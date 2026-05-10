# Phase 10. 채점 신뢰도 운영화 계획

## 현재 완료 상태

- 전체 362문제에 override가 존재한다.
- `npm run judge:coverage` 기준 `sampleOnly = 0`이다.
- Docker runner 기준 `npm run judge:verify-overrides` 전체 통과를 확인했다.
- Python, C++, Java 기준 소스가 실제 runner 경로에서 실행 가능함을 확인했다.

## 다음 목표

채점 데이터가 “존재한다”에서 끝나는 것이 아니라, 운영 중에도 깨지지 않도록 자동 검증과 운영 절차를 만든다.

## Phase 10-1. CI 검증 분리

목표:

- GitHub Actions에서 빠른 검증과 느린 검증을 분리한다.

작업:

- PR마다 실행할 빠른 검증:
  - `npm run judge:coverage`
  - `npm run harness:test`
  - override import / expected 생성 검증
- 수동 또는 nightly로 실행할 느린 검증:
  - Docker image build
  - `npm run judge:verify-overrides`

이유:

- 전체 Docker 검증은 약 40분 이상 걸릴 수 있다.
- 모든 PR에서 전체 검증을 강제하면 개발 속도가 크게 떨어진다.

## Phase 10-2. Judge Server Docker 운영 모드 고정

목표:

- 운영에서는 LocalRunner가 아니라 DockerRunner를 기본으로 사용한다.

작업:

- `.env.example`에 운영 권장값 명확화:
  - `JUDGE_USE_DOCKER=1`
  - `CODERUNNER_IMAGE=dongjun-coderunner:latest`
- 서버 시작 전 Docker image 존재 여부 체크.
- Docker daemon 미실행 시 명확한 에러 메시지 제공.

## Phase 10-3. 제출 결과 저장 강화

목표:

- 사용자가 어떤 케이스에서 실패했는지 추적 가능하게 만든다.

작업:

- SQLite 제출 테이블에 다음 값 저장 여부 확인:
  - verdict
  - language
  - problem slug
  - failed case kind
  - duration
  - created_at
- 실패한 case의 전체 input/output은 너무 클 수 있으므로, preview만 저장하거나 별도 파일 저장으로 분리한다.

## Phase 10-4. TLE/MLE/OLE 전용 회귀 테스트

목표:

- 정답성뿐 아니라 실행 제한 판정이 제대로 동작하는지 검증한다.

작업:

- 의도적으로 무한 루프를 도는 Python/C++ 코드로 TLE 확인.
- 큰 메모리를 할당하는 코드로 MLE 확인.
- 무한 출력 코드로 OLE 확인.
- 컴파일 실패 코드로 CE 확인.

성공 기준:

```txt
TLE -> TLE
MLE -> MLE
OLE -> OLE
CE  -> CE
RE  -> RE
```

## Phase 10-5. 문제별 override 품질 점수화

목표:

- 모든 override가 존재하더라도 품질 차이를 추적한다.

점수 기준:

- sample 포함 여부
- 최소 입력 포함 여부
- 경계값 포함 여부
- stress case 포함 여부
- 여러 정답 가능성 처리 여부
- special judge 필요 여부

출력 예:

```txt
problem,case_count,has_edge,has_stress,needs_special_judge,risk
implementation-16926,9,true,true,false,low
disjoint_set-17352,6,true,true,true,medium
```

## Phase 10-6. 배포 전 체크리스트

운영 서버 배포 전에 아래 순서로 확인한다.

```txt
npm install
npm run build
docker build -t dongjun-coderunner:latest judge
npm run judge:coverage
npm run harness:test
npm run judge:verify-overrides
```

이후 서버에서는:

```txt
JUDGE_USE_DOCKER=1
CODERUNNER_IMAGE=dongjun-coderunner:latest
```

## 우선순위

1. CI 빠른 검증 추가
2. TLE/MLE/OLE/CE/RE 회귀 테스트 추가
3. 운영 Docker 모드 체크 강화
4. 제출 결과 저장 구조 점검
5. override 품질 점수화

## 작업 로그

### 2026-05-10

진행:

- PR/push용 빠른 CI workflow 추가:
  - `.github/workflows/ci.yml`
  - `npm run ops:check-env:example`
  - `npm run judge:coverage`
  - `npm run judge:lang-audit`
  - `npm run harness:test`
- 수동/nightly Docker 전체 검증 workflow 추가:
  - `.github/workflows/judge-docker-nightly.yml`
  - Docker image build
  - `npm run judge:docker-check`
  - `npm run judge:verify-overrides`
- Docker runner smoke check 스크립트 추가:
  - `scripts/check-docker-runner.py`
  - Python/C++/Java 코드가 실제 coderunner 이미지에서 실행되는지 확인
- Docker verdict 회귀 테스트 추가:
  - `harness/tests/test_docker_runner_verdicts.py`
  - CE, RE, TLE, MLE, OLE 판정 경로 확인

설계 결정:

- 전체 override 검증은 약 40분 이상 걸릴 수 있으므로 PR CI에는 넣지 않는다.
- Docker verdict 테스트는 Docker daemon이 없으면 skip한다.
- 운영 배포 전 또는 nightly에서는 Docker daemon과 coderunner image가 있는 환경에서 전체 검증을 수행한다.

검증 결과:

```txt
npm run ops:check-env:example
-> Environment check passed.

npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 362
-> sampleOnly 0
-> highRiskSampleOnly 0

npm run judge:lang-audit
-> allProblemsAcceptPythonCpp true
-> dockerCliAvailable true

npm run harness:test
-> OK, 14 tests

npm run judge:docker-check
-> Docker runner check passed.
```

주의:

- `judge:docker-check`의 C++/Java 컴파일 smoke test는 512MB 메모리 제한으로 실행한다.
- 실제 제출 채점은 문제별 제한값을 별도 정책으로 정해야 한다.
