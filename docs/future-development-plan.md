# DongJun CodeDex 개발 로드맵

작성일: 2026-05-01

## 현재 앱 요약

DongJun CodeDex는 BOJ 기반 코딩테스트 학습 앱입니다. Next.js App Router로 화면과 API를 만들고, Python judge 서버가 사용자 코드를 실행해 oracle 코드 출력과 비교합니다. 문제는 알고리즘 분류별로 포켓몬/도감 컨셉에 매핑되어 있고, 사용자는 문제를 풀면서 TR, 포획 기록, 리더보드 기록을 쌓습니다.

현재 구성은 다음과 같습니다.

- `app/`: 홈, 카테고리, 문제 풀이, 프로필, 리더보드 페이지와 API 라우트
- `components/`: Monaco 기반 풀이 화면, 트레이너 상태, 포획 애니메이션, 카드 UI
- `lib/`: 문제 데이터 로더, 캐릭터/풍미 텍스트, 레이팅, SQLite 저장소, 세션 쿠키
- `harness/`: 테스트케이스 생성기, oracle 비교 채점 코어, 일부 문제별 override
- `judge/`: Python HTTP judge 서버와 Docker 기반 코드 실행 이미지
- `data/`: BOJ 문제/메타/문제문/도감 매핑 JSON
- `e2e/`: Playwright smoke test

## 먼저 개선하면 좋은 것

### 1. 한글 인코딩 복구

현재 README, 페이지 텍스트, 주석, 테스트명이 깨진 문자로 보입니다. 사용자가 가장 먼저 체감하는 문제라 우선순위가 높습니다.

작업 방향:

- 깨진 한글 UI 문구를 정상 한국어로 복구
- `README.md`, `judge/README.md`, 주요 컴포넌트의 안내문/버튼/테이블 헤더 수정
- Playwright 테스트의 접근성 이름도 정상 문구 기준으로 수정
- 파일 인코딩을 UTF-8로 통일하고, Windows/PowerShell에서 깨지지 않는 편집 규칙 정리

### 2. 문제 풀이 UX 강화

현재 `ProblemPlayground`는 코드 작성, 제출, 결과 표시가 가능한 핵심 기능을 갖고 있습니다. 다음 기능을 추가하면 실제 코딩테스트 연습 도구로 더 좋아집니다.

- 코드 자동 저장: 문제/언어별 draft를 DB 또는 localStorage에 저장
- 제출 전 실행: 샘플 입력 직접 실행 기능
- 채점 결과 상세화: 첫 실패 케이스, stdout/stderr, 시간, 메모리, verdict 설명 분리
- 제출 기록 탭: 같은 문제의 이전 제출 코드와 결과 확인
- 언어별 템플릿 개선: Python, C++, Java 템플릿을 BOJ 스타일로 정리
- Monaco 단축키: `Ctrl+Enter` 제출, `Ctrl+S` 저장

### 3. 채점 정확도 개선

현재 채점은 category 기반 fuzz input을 만들고 oracle 출력과 비교합니다. 프로토타입으로는 좋지만, 실제 문제별 입력 형식과 다를 수 있어 오답/정답 판정 신뢰도가 흔들릴 수 있습니다.

작업 방향:

- 문제별 sample test를 `data/problems-statements.json`에서 추출해 우선 실행
- `harness/overrides/<slug>.py`를 늘려 주요 문제부터 정확한 generator 제공
- generator 실패 또는 oracle 실패 시 `ERR`/`generator error`로 분리
- 케이스 종류를 `sample`, `custom`, `fuzz`로 명확히 구분
- 채점 로그를 남겨 재현 가능한 seed와 입력을 확인할 수 있게 하기

### 4. 보안/악용 방지

사용자 코드 실행 앱이므로 배포 전에 보안을 조금 더 단단히 해야 합니다.

- Next API의 `/api/judge`에 rate limit 추가
- 코드 길이, 요청 body 크기, 제출 빈도 제한을 환경변수화
- judge 서버는 외부 공개 금지, 반드시 `127.0.0.1` 또는 내부 네트워크만 허용
- Docker runner 이미지에 seccomp/cap-drop/no-new-privileges 옵션 추가 검토
- oracle 코드는 신뢰 코드지만, 장기적으로 oracle 실행도 격리하는 방향 고려
- 제출 코드와 실패 로그 저장 시 개인정보/세션 정보가 섞이지 않게 필터링

### 5. 계정/세션 모델 정리

현재는 이름 + secret 쿠키 기반의 간단한 트레이너 세션입니다. 혼자 쓰거나 로컬 데모에는 충분하지만, 공개 서비스로 갈수록 계정 모델이 필요합니다.

- 닉네임 중복 처리 UX 개선
- 세션 만료/재로그인/다른 기기 이전 기능
- 게스트 모드와 정식 계정 모드 분리
- 사용자별 제출 코드 저장 여부 선택
- 관리자용 유저/제출/채점 상태 확인 페이지

## 기능 확장 아이디어

### 학습 기능

- 알고리즘별 추천 경로: 쉬운 문제에서 어려운 문제로 이어지는 로드맵
- 약점 분석: WA/TLE가 많은 유형을 프로필에서 보여주기
- 힌트 단계: 1단계 접근법, 2단계 자료구조, 3단계 의사코드
- 복습 큐: 틀렸거나 오래 전에 푼 문제를 다시 추천
- 문제 즐겨찾기/나중에 풀기

### 게임화 기능

- 포획 도감 완성도 보상
- 카테고리별 배지/칭호
- 연속 학습 streak
- 레이드 문제: 어려운 문제를 제한 시간 안에 도전
- 시즌 리더보드와 전체 리더보드 분리

### 운영 기능

- 문제 데이터 갱신 스크립트 정기 실행
- 깨진 이미지/메타데이터 검증 자동화
- 채점 실패율이 높은 문제 모니터링
- admin-only 문제 비활성화 플래그
- 사용자 신고 또는 문제 오류 제보 기능

## 데이터/DB 발전 계획

현재 SQLite는 로컬/소규모 운영에 적합합니다. 운영 규모가 커지면 다음 순서로 발전시키는 것이 좋습니다.

1. SQLite 유지 단계
   - `.data/dongjun.db` 백업 스크립트 추가
   - DB schema migration 파일 도입
   - leaderboard/history 쿼리 인덱스 점검

2. 서버 1대 운영 단계
   - SQLite WAL 유지
   - DB 파일을 앱 배포 디렉터리 밖의 persistent volume에 저장
   - 주기적 백업과 복구 리허설 추가

3. 다중 서버 또는 컨테이너 확장 단계
   - PostgreSQL로 이전
   - Prisma/Drizzle 같은 migration 도구 도입 검토
   - 세션 저장소를 DB 또는 Redis로 통합

## 배포 로드맵

### Phase 0. 로컬 개발 안정화

목표: 지금 로컬에서 재현 가능하게 돌아가는 상태를 명확히 만들기.

- `npm run dev`와 `python judge/server.py` 실행 문서 정리
- Docker runner 이미지 빌드 명령 확인
- `npm run build`, `npm run e2e`, `npm run harness:test` 통과 기준 정리
- `.env.example` 추가

권장 환경변수:

```bash
JUDGE_URL=http://127.0.0.1:5050/judge
JUDGE_PORT=5050
JUDGE_USE_DOCKER=1
CODERUNNER_IMAGE=dongjun-coderunner:latest
NODE_ENV=production
```

### Phase 1. 단일 서버 프로덕션 실행

목표: 한 대의 서버에서 Next.js와 judge를 같이 띄우기.

구성:

- Next.js: `127.0.0.1:3000`
- judge: `127.0.0.1:5050`
- Nginx: 외부 `80/443` 수신 후 Next.js로 reverse proxy
- Docker: 사용자 코드 실행 전용 runner image
- SQLite: 서버의 persistent directory에 저장

운영 명령 예시:

```bash
npm ci
npm run build
docker build -t dongjun-coderunner:latest judge
JUDGE_USE_DOCKER=1 python judge/server.py
npm run start
```

실제로는 `systemd` 또는 `pm2`로 Next.js와 judge를 서비스화하는 것을 권장합니다.

### Phase 2. Nginx reverse proxy 적용

목표: 외부 사용자는 Nginx만 보게 하고, 내부 서비스는 localhost로 숨기기.

예시 Nginx 설정:

```nginx
server {
    listen 80;
    server_name example.com;

    client_max_body_size 512k;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

주의:

- `/api/judge`를 Nginx에서 judge 서버로 직접 보내지 말고, Next.js API를 거치게 두는 편이 안전합니다.
- judge 서버 포트 `5050`은 방화벽에서 외부 접근을 막아야 합니다.
- HTTPS 적용 후 session cookie의 `secure` 옵션이 정상 동작하는지 확인해야 합니다.

### Phase 3. HTTPS와 운영 안정화

목표: 실제 사용자에게 공개 가능한 기본 운영 상태 만들기.

- Let's Encrypt 인증서 적용
- HTTP에서 HTTPS로 redirect
- Nginx access/error log rotation
- `systemd` restart policy 설정
- 배포 후 health check 경로 추가: 예: `/api/health`
- judge health check 추가: 예: `GET /health`
- 서버 재부팅 후 자동 시작 확인

### Phase 4. 컨테이너 기반 운영

목표: 서버 재현성과 배포 안정성 향상.

권장 컨테이너 분리:

- `web`: Next.js app
- `judge`: Python judge HTTP server
- `runner-image`: 사용자 코드 실행용 이미지
- `nginx`: reverse proxy
- `db-volume`: SQLite 또는 PostgreSQL 데이터

Docker Compose로 묶되, judge는 내부 네트워크에만 노출합니다.

### Phase 5. 확장 운영

목표: 사용자 증가에 대비.

- PostgreSQL 이전
- Redis 기반 rate limit/queue 도입
- 채점 요청 큐 분리: API가 요청을 enqueue하고 worker가 채점
- 제출 결과 polling 또는 websocket/SSE 제공
- 채점 worker 수평 확장
- 문제 데이터/이미지 CDN 캐싱

## Nginx 전환 전 체크리스트

- `npm run build`가 안정적으로 통과한다.
- `npm run start`로 production 모드 실행이 된다.
- judge가 `127.0.0.1:5050`에서만 열린다.
- `JUDGE_URL`이 production 환경에서 정확히 설정되어 있다.
- `.data/dongjun.db` 위치와 백업 정책이 정해져 있다.
- 서버 방화벽에서 `80`, `443`, `ssh` 외 포트를 닫았다.
- `/api/judge` 요청 크기와 빈도 제한이 있다.
- Docker runner image가 서버에서 빌드 또는 pull 가능하다.
- 로그 위치와 장애 시 재시작 방법이 문서화되어 있다.

## 추천 우선순위

1. 한글 인코딩/UI 문구 복구
2. `.env.example`, 실행 문서, 배포 문서 정리
3. 문제별 sample/custom/fuzz 채점 구조 개선
4. 제출 기록과 코드 자동 저장
5. Nginx + systemd 기반 단일 서버 배포
6. rate limit, health check, 로그/백업
7. PostgreSQL/큐/worker 기반 확장

이 순서로 가면 지금 앱의 재미있는 핵심은 유지하면서, 로컬 토이 프로젝트에서 공개 가능한 학습 서비스로 자연스럽게 넘어갈 수 있습니다.
