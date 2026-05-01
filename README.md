# DongJun CodeDex 🎮

> 백준이 닫혀서 만든, **포켓몬 도감 컨셉**의 코딩테스트 학습 사이트.
> 22개 알고리즘 분류 = 18개 포켓몬 타입, 362마리의 코드 몬스터를 잡아 진화시키세요.

## 컨셉
- **분류** → 포켓몬 **타입** (그리디=불꽃, DP=에스퍼, 그래프=비행 …)
- **문제** → 한 마리의 **몬스터** (해시 기반 결정적 이름/스탯/희귀도/진화단계)
- **풀이** → 야생몬스터와 **전투** → 통과하면 도감에 등록(추후)

## 하네스 엔지니어링
BOJ 솔루션 폴더에는 정답 코드만 있고 테스트케이스가 없습니다. 이걸 역이용:

```
사용자 코드 ─┐
            ▼
       [동일 입력] ──► 결과 비교 ──► AC/WA
            ▲
정답코드(Oracle) ┘
```

1. **입력 생성기**(`harness/generators.py`): 카테고리별 템플릿 + 문제별 override 로 결정적 입력 N개 생성.
2. **Oracle 실행기**: BOJ 정답 코드를 그 입력으로 실행 → 기대 출력.
3. **사용자 실행기**: Docker 샌드박스(`--network=none --read-only` 등)에서 사용자 코드 실행.
4. **비교**: 공백/개행 정규화 후 일치 여부.
5. **단위 테스트**(`harness/tests/`)와 **E2E**(`e2e/`)로 하네스 자체를 검증.

## 디렉토리
```
app/                Next.js (App Router) — 도감/카테고리/문제 페이지 + /api/judge
components/         ProblemPlayground (Monaco 에디터 + 결과 패널)
lib/                types · dataset 로더 · characters (몬스터 매핑)
data/               index-boj 산출물 (categories.json / problems.json) — 빌드 시 생성
scripts/            BOJ 인덱서 (Node, fs 스캔)
harness/            입력 생성기 + 채점 코어 + 단위테스트 + 문제별 override
judge/              Docker 샌드박스 채점 서비스 (Python HTTP 서버 + Dockerfile)
e2e/                Playwright 스모크 테스트
```

## 시작
```bash
# 0) BOJ 클론이 ../BOJ/baekjoon 에 있다고 가정 (없으면 BOJ_ROOT 환경변수)
npm install
npm run index:boj         # data/categories.json, data/problems.json 생성
npm run dev               # http://localhost:3000

# (선택) 채점 백엔드
cd judge && docker build -t dongjun-coderunner:latest . && cd ..
JUDGE_USE_DOCKER=1 python judge/server.py    # 다른 터미널

# 검증
python -m unittest harness/tests/test_judge.py
npm run e2e:install && npm run e2e
```

## 환경변수
| 변수 | 기본값 |
|---|---|
| `BOJ_ROOT` | `../BOJ/baekjoon` (인덱서가 사용) |
| `JUDGE_URL` | `http://127.0.0.1:5050/judge` (Next → judge) |
| `JUDGE_PORT` | `5050` |
| `JUDGE_USE_DOCKER` | `1` (0=LocalRunner, 개발용·위험) |

## 보안 (OWASP)
- 사용자 코드는 Next.js 프로세스/호스트에서 절대 실행 X — 격리 컨테이너 전용
- 코드 길이 제한, 언어 화이트리스트, 컨테이너 자원 제한(memory/pids/nofile)
- judge 서버는 `127.0.0.1` 바인딩 (외부 노출 금지)

## 다음 단계 아이디어
- 도전 통과 시 localStorage 도감 등록 + 진화 애니메이션
- 문제별 override 더 확보(특히 그래프/문자열 계열)
- AI 보조 풀이(서버측 키 보호, 별도 라우트)
