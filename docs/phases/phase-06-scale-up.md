# Phase 06. 확장 구조 준비

## 목표

사용자가 늘어났을 때를 대비해 DB, 채점 worker, 큐, 캐시 구조로 확장할 수 있는 방향을 준비합니다.

## 범위

- SQLite에서 PostgreSQL로 이전하는 기준 정리
- migration 도구 검토
- 카카오/네이버 간편 로그인 기반 계정 구조 설계
- Redis 기반 rate limit/queue 설계
- judge worker 분리 설계
- 제출 결과 polling 또는 SSE/WebSocket 설계
- 이미지/정적 데이터 캐싱 전략 정리

## 완료 기준

- 단일 서버 구조에서 다중 서버 구조로 넘어가는 판단 기준이 있다.
- DB migration 방향이 문서화되어 있다.
- judge queue/worker 구조의 책임 분리가 명확하다.

## 작업 로그

- 운영 서버로 옮기기 전에 환경변수 오류를 빠르게 잡을 수 있도록 `scripts/check-env.mjs`를 추가했습니다.
- `package.json`에 `npm run ops:check-env` 스크립트를 추가했습니다.
- 현재 단계에서는 Oracle VM 생성은 하지 않고, 로컬/운영 공통으로 쓸 수 있는 사전 점검 도구를 먼저 준비합니다.
- Docker Desktop 엔진을 켠 뒤 로컬 judge 서버와 Next.js dev 서버를 함께 실행했습니다.
- 신규 브라우저 세션/기기에서도 같은 트레이너로 이어서 플레이할 수 있도록 소셜 로그인 기반 계정 전환 계획을 추가합니다.
- `auth_accounts` 테이블과 카카오/네이버 OAuth 시작/콜백 API 뼈대를 추가했습니다.
- 프로필 화면에 `카카오로 기록 보관하기`, `네이버로 기록 보관하기` 진입점을 추가했습니다.
- `npm run ops:check-env`가 실제 `.env`를 검사하도록 변경하고, 예시 파일 검사는 `npm run ops:check-env:example`로 분리했습니다.
- 공통 category fuzz generator를 기본 비활성화했습니다. 이제 기본 채점은 BOJ 샘플과 문제별 override만 사용합니다.
- 전체 문제의 샘플/override 준비 상태를 확인하는 `npm run judge:audit` 스크립트를 추가했습니다.

## 실행 결과(Output)

```bash
npm run ops:check-env
```

성공 시:

```txt
Environment check passed.
```

로컬 실행 세션:

```txt
judge health: ok=true, docker=true, maxConcurrentJobs=3
web health: ok=true, service=dongjun-web
Next.js: http://127.0.0.1:3000
Judge: http://127.0.0.1:5050
```

소셜 로그인 기반 작업:

```txt
DB: auth_accounts 테이블 추가
API: /api/auth/kakao/start, /api/auth/kakao/callback
API: /api/auth/naver/start, /api/auth/naver/callback
API: /api/auth/accounts
UI: 프로필 화면 기록 보관 CTA 추가
```

Judge 안정화 작업:

```txt
기본 정책: sample case + problem-specific override
비활성화: category generic fuzz
이유: 문제별 입력 형식을 모르는 generic fuzz가 oracle failure를 만들 수 있음
예외: JUDGE_ENABLE_GENERIC_FUZZ=1 설정 시 실험적으로 generic fuzz 사용 가능
```

전체 audit 결과:

```txt
total: 362
judgeReady: 329
missingCases: 33
report: docs/judge-case-audit.md
```

## 소셜 로그인 계정 계획

현재 문제:

- `dj_session` 쿠키는 브라우저 세션을 식별하는 데는 충분하지만, 쿠키가 삭제되거나 다른 기기에서 접속하면 같은 트레이너를 복구할 수 없습니다.
- 오박사의 "너의 이름이 뭐였더라?" 온보딩 컨셉은 좋지만, 이미 가입한 사용자가 매번 새 이름을 입력해야 하면 계정 경험이 깨집니다.

목표:

- 첫 방문 경험은 기존처럼 오박사의 "너의 이름이 뭐였더라?" 온보딩으로 시작합니다.
- 사용자는 먼저 트레이너 이름을 정하고 로컬 세션으로 바로 문제를 풀 수 있습니다.
- 이후 프로필/HUD에서 `카카오로 기록 보관하기` 또는 `네이버로 기록 보관하기`를 제공해 현재 trainer_id를 소셜 계정과 연결합니다.
- 재방문 또는 새 기기에서는 카카오/네이버 로그인을 통해 기존 trainer_id를 복구합니다.

권장 흐름:

```txt
첫 방문
  -> 오박사 온보딩
  -> "너의 이름이 뭐였더라?"
  -> 트레이너 이름 입력
  -> 로컬 세션 생성
  -> 바로 문제 풀이 가능

이후
  -> 프로필/HUD에 "카카오로 기록 보관하기" 또는 "네이버로 기록 보관하기" 노출
  -> 사용자가 선택하면 소셜 로그인 창으로 이동
  -> OAuth 인증
  -> provider + provider_user_id 확인
  -> 현재 trainer_id와 소셜 계정 연결

소셜 로그인 연결
  -> Kakao/Naver OAuth 인증
  -> provider + provider_user_id 확인
  -> 현재 trainer_id와 연결
  -> 이후 어느 기기에서 로그인해도 같은 trainer_id 복구

재방문/새 기기
  -> dj_session 쿠키가 있으면 바로 진행
  -> 쿠키가 없으면 "카카오/네이버로 이어하기" 제공
  -> 로그인 성공 시 기존 trainer_id 복구
  -> 기존 TR, 포획 기록, 제출 기록 그대로 이어서 진행
```

예상 DB 확장:

```sql
CREATE TABLE auth_accounts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  trainer_id INTEGER NOT NULL REFERENCES trainers(id) ON DELETE CASCADE,
  provider TEXT NOT NULL,
  provider_user_id TEXT NOT NULL,
  email TEXT,
  display_name TEXT,
  created_at INTEGER NOT NULL,
  last_login_at INTEGER NOT NULL,
  UNIQUE(provider, provider_user_id)
);
```

예상 API:

```txt
GET /api/auth/kakao/start
GET /api/auth/kakao/callback
GET /api/auth/naver/start
GET /api/auth/naver/callback
POST /api/auth/logout
GET /api/me
```

환경변수:

```env
KAKAO_REST_API_KEY=
KAKAO_CLIENT_SECRET=
KAKAO_REDIRECT_URI=
NAVER_CLIENT_ID=
NAVER_CLIENT_SECRET=
NAVER_REDIRECT_URI=
AUTH_SESSION_SECRET=
```

구현 순서:

1. `auth_accounts` 테이블 추가
2. OAuth `state` 생성/검증 추가
3. 프로필/HUD에 "기록 보관하기" CTA 위치 설계
4. 카카오 로그인부터 연결
5. 네이버 로그인 추가
6. 기존 쿠키 세션과 소셜 계정 연결
7. 쿠키가 없는 재방문자에게 "카카오/네이버로 이어하기" 제공
8. 프로필 화면에 로그인 상태와 계정 연결 상태 표시
9. 로그아웃과 계정 연결 해제 정책 정리

참고한 공식 문서:

- Kakao Login REST API: https://developers.kakao.com/docs/latest/en/kakaologin/rest-api
- Kakao REST API reference: https://developers.kakao.com/docs/latest/en/rest-api/reference
- NAVER Login overview: https://developers.naver.com/docs/login/overview/overview.md
- NAVER Open API list: https://naver.github.io/naver-openapi-guide/apilist.html

## 예상 리스크

- PostgreSQL 도입 시 기존 SQLite 데이터 이전 스크립트가 필요합니다.
- worker 분리 후에는 채점 결과 동기화 방식이 바뀌므로 UI/API 계약을 다시 잡아야 합니다.
