# Phase 00. 현재 상태 점검과 개발 기준선 만들기

## 목표

큰 개발을 시작하기 전에 현재 앱의 구조, 실행 방식, 검증 명령, 문서 기록 방식을 정리합니다. 이 phase는 이후 작업의 기준점 역할을 합니다.

## 범위

- phase별 개발 문서 구조 생성
- 현재 앱 구조 요약
- 앞으로 사용할 검증 명령 정리
- 현재 기준선에서 실행 가능한 테스트 확인
- 이후 phase 우선순위 확정

## 완료 기준

- `docs/phases/` 아래에 phase별 문서가 생성되어 있다.
- 각 phase 문서에 목표, 범위, 완료 기준, 실행 결과 섹션이 있다.
- 현재 상태에서 실행한 검증 명령 결과가 이 문서에 기록되어 있다.

## 현재 앱 기준선

현재 앱은 다음 구성으로 되어 있습니다.

- Next.js App Router 기반 웹 앱
- Monaco Editor 기반 문제 풀이 화면
- `/api/judge`를 통한 judge 서버 프록시
- Python `judge/server.py`와 `harness/judge_core.py` 기반 채점 코어
- Docker runner 이미지로 사용자 코드 실행 격리
- SQLite 기반 트레이너/포획/시도/히스토리 저장
- Playwright smoke test와 Python harness unit test 보유

## 앞으로 기본 검증 명령

```bash
npm run build
npm run e2e
npm run harness:test
```

상황별 추가 검증:

```bash
npm run dev
python judge/server.py
docker build -t dongjun-coderunner:latest judge
```

## 작업 로그

- `docs/phases/` 폴더를 생성했다.
- phase별 문서 파일을 만들었다.
- 각 phase마다 실행 결과를 남길 수 있는 섹션을 마련했다.
- 기준선 검증 명령을 실행했다.
- `npm run build`는 성공했다.
- `npm run harness:test`는 현재 Python 환경에 `pytest`가 설치되어 있지 않아 실패했다.

## 실행 결과(Output)

### 1. Git 상태 확인

명령:

```bash
git status --short --branch
```

결과 요약:

```text
## main...origin/main
```

의미:

- 로컬 브랜치 `main`은 원격 `origin/main`을 추적하고 있다.
- Phase 00 작업 전에는 커밋되지 않은 변경이 없었다.

### 2. Python harness 테스트

명령:

```bash
npm run harness:test
```

결과:

```text
> dongjun-codedex@0.1.0 harness:test
> python -m pytest harness/tests -q

C:\Users\pcuser\miniconda3\python.exe: No module named pytest
```

판단:

- 테스트 코드 실행까지 가지 못했다.
- 실패 원인은 앱 코드가 아니라 현재 Python 환경에 `pytest` 패키지가 없는 것이다.
- 다음 작업 중 하나가 필요하다.
  - 개발 환경에 `pytest` 설치
  - Python 의존성 파일(`requirements-dev.txt` 등) 추가
  - `package.json`의 테스트 스크립트와 문서에 Python 준비 절차 명시

### 3. Next.js production build

명령:

```bash
npm run build
```

결과 요약:

```text
[index-boj] categories: 22, problems: 362
[pokedex] using cached data/pokedex.json (1025 entries)
[monster-map] 362 mappings
✓ Compiled successfully
✓ Generating static pages (392/392)
```

주요 route:

```text
/                         static
/category/[slug]          SSG, 22 paths
/problem/[slug]           SSG, 362 paths
/api/judge                dynamic
/api/leaderboard          dynamic
/api/trainer/*            dynamic
/profile                  static/client
/leaderboard              static/client
```

판단:

- 현재 기준선에서 production build는 성공한다.
- `data:all` 스크립트도 정상 실행된다.
- `.next/` 산출물은 `.gitignore`로 추적되지 않는다.

### 4. 작업 후 Git 상태

명령:

```bash
git status --short
```

결과 요약:

```text
?? docs/phases/
```

판단:

- 이번 phase에서 새로 만든 문서만 추적되지 않은 변경으로 남아 있다.
- 빌드/데이터 생성으로 인한 추적 파일 변경은 없다.

## 다음 단계

Phase 01에서 깨진 한글 문구를 복구합니다. 사용자가 보는 화면, README, judge README, Playwright 테스트명을 우선 정리합니다.
