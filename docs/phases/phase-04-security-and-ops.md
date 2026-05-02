# Phase 04. 보안과 운영 안전장치

## 목표

사용자 코드를 실행하는 서비스이므로 공개 운영 전에 기본 보안 장치와 운영 관측성을 추가합니다.

## 범위

- `/api/judge` rate limit 추가
- 요청 body/code/stdin size 제한 환경변수화
- `/api/health` 추가
- judge 서버 `/health` endpoint 추가
- Docker runner 보안 옵션 강화
- judge 동시 실행 제한 추가
- Docker Desktop/WSL2 실행 전제 확인
- SQLite 백업 스크립트 추가
- SQLite write 대기 설정 추가
- 운영 환경변수 문서화

## 완료 기준

- 과도한 제출 요청이 제한된다.
- 웹 서버와 judge 서버 상태를 health check로 확인할 수 있다.
- 운영에 필요한 환경변수가 문서화되어 있다.
- Docker runner가 실제 Docker Desktop 환경에서 동작한다.
- judge 서버가 동시에 실행할 job 수를 제한한다.
- SQLite write lock 충돌 시 일정 시간 대기한다.
- SQLite DB 백업 명령이 동작한다.
- `npm run build`, `npm run harness:test`, `npm run e2e`가 통과한다.

## 작업 로그

### 1. Docker Desktop 준비 상태 갱신

이전에 Docker Desktop은 아래 오류로 시작하지 못했습니다.

```text
Virtualization support not detected
Docker Desktop failed to start because virtualisation support wasn’t detected.
```

2026-05-03 현재 상태:

```text
Docker Desktop 4.71.0
Docker Engine 29.4.1
WSL Ubuntu Running, VERSION 2
docker-desktop Running, VERSION 2
```

판단:

- Docker Desktop과 WSL2 backend가 정상 동작합니다.
- 이제 로컬에서도 `JUDGE_USE_DOCKER=1` 기준으로 사용자 코드 실행을 검증할 수 있습니다.

### 2. Web health check 추가

추가 파일:

```text
app/api/health/route.ts
```

응답 예:

```json
{
  "ok": true,
  "service": "dongjun-web",
  "uptimeSec": 12,
  "timestamp": "2026-05-03T..."
}
```

용도:

- Nginx, systemd, uptime monitor에서 웹 앱 상태를 확인할 때 사용합니다.

### 3. Judge health check 추가

변경 파일:

```text
judge/server.py
```

추가 endpoint:

```text
GET /health
```

응답 예:

```json
{
  "ok": true,
  "service": "dongjun-judge",
  "docker": true,
  "uptimeSec": 0
}
```

용도:

- judge 서버가 살아 있는지 확인합니다.
- 현재 judge가 Docker runner 모드인지 확인할 수 있습니다.

### 4. `/api/judge` rate limit 추가

변경 파일:

```text
app/api/judge/route.ts
```

추가 내용:

- in-memory per-IP rate limit
- 기본값: 60초에 20회
- 초과 시 HTTP `429`와 `retry-after` header 반환

환경변수:

```text
JUDGE_RATE_LIMIT_WINDOW_MS=60000
JUDGE_RATE_LIMIT_MAX=20
```

주의:

- 현재 방식은 단일 Next.js 프로세스 기준입니다.
- 여러 서버/여러 인스턴스로 확장하면 Redis 같은 shared store로 바꿔야 합니다.

### 5. 요청 크기 제한 환경변수화

추가/변경 환경변수:

```text
JUDGE_MAX_CODE_BYTES=65536
JUDGE_MAX_STDIN_BYTES=65536
JUDGE_MAX_BODY_BYTES=262144
```

의미:

- `JUDGE_MAX_CODE_BYTES`: 제출 코드 최대 크기
- `JUDGE_MAX_STDIN_BYTES`: 직접 실행 custom input 최대 크기
- `JUDGE_MAX_BODY_BYTES`: judge 서버가 받는 HTTP body 최대 크기

### 6. Docker runner 보안 옵션 강화

변경 파일:

```text
harness/judge_core.py
judge/entrypoint.sh
```

추가/변경한 Docker 실행 옵션:

```text
--network none
--read-only
--cap-drop ALL
--security-opt no-new-privileges
--tmpfs /work:exec,size=64m,mode=1777
--memory <limit>
--memory-swap <limit>
--cpus 1.0
--pids-limit 128
--ulimit nofile=64:64
```

중간에 발견한 문제:

- `--tmpfs /work`가 root 소유로 올라와서 `runner` 사용자가 `/work`에 파일을 복사하지 못했습니다.
- 기존 `entrypoint.sh`가 `cp ... || true`로 복사 실패를 숨기고 있어 원인 파악이 늦어질 수 있었습니다.

조치:

- tmpfs에 `mode=1777`을 부여했습니다.
- `entrypoint.sh`에서 복사 실패를 숨기지 않도록 바꿨습니다.
- Windows Docker Desktop mount 안정성을 위해 runner 임시 디렉터리를 기본적으로 `.data/runner-tmp` 아래에 만들도록 바꿨습니다.

### 7. 운영 환경변수 샘플 추가

추가 파일:

```text
.env.example
```

주요 내용:

```text
JUDGE_URL=http://127.0.0.1:5050/judge
JUDGE_RUN_URL=http://127.0.0.1:5050/run
JUDGE_PORT=5050
JUDGE_USE_DOCKER=1
CODERUNNER_IMAGE=dongjun-coderunner:latest
```

### 8. SQLite 백업 스크립트 추가

추가 파일:

```text
scripts/backup-sqlite.ps1
```

사용 예:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\backup-sqlite.ps1
```

기본 동작:

- `.data\dongjun.db`를 `.data\backups\dongjun-YYYYMMDD-HHMMSS.db`로 복사합니다.
- `.data/`는 `.gitignore` 대상이므로 백업 파일은 Git에 올라가지 않습니다.

### 9. 다중 유저 최소 안전장치 추가

변경 파일:

```text
judge/server.py
lib/db.ts
.env.example
```

judge 동시 실행 제한:

```text
JUDGE_MAX_CONCURRENT_JOBS=3
JUDGE_JOB_ACQUIRE_TIMEOUT_S=2.0
```

의미:

- 동시에 실행되는 Docker judge job 수를 제한합니다.
- 기본값은 3개입니다.
- 제한 시간 안에 실행 슬롯을 얻지 못하면 HTTP `503`과 `judge busy, retry later`를 반환합니다.

SQLite write 대기:

```ts
d.pragma("busy_timeout = 5000");
```

의미:

- 여러 사용자의 기록 저장이 겹칠 때 SQLite가 바로 실패하지 않고 최대 5초 대기합니다.
- 소규모 단일 서버 운영에서 write lock 충돌을 줄이는 안전장치입니다.

## 실행 결과(Output)

### 1. Docker Desktop 확인

명령:

```powershell
docker version
wsl -l -v
docker run --rm hello-world
```

결과 요약:

```text
Docker Desktop 4.71.0
Docker Engine 29.4.1
Ubuntu Running VERSION 2
docker-desktop Running VERSION 2
Hello from Docker!
```

판단:

- Docker Desktop과 WSL2가 정상 동작합니다.

### 2. Runner 이미지 빌드

명령:

```powershell
docker build -t dongjun-coderunner:latest judge
```

결과:

```text
naming to docker.io/library/dongjun-coderunner:latest done
```

판단:

- 사용자 코드 실행용 Docker 이미지가 정상 빌드됩니다.

### 3. Docker runner 기반 judge smoke

명령 요약:

```powershell
JUDGE_USE_DOCKER=1
JUDGE_PORT=5066
python judge/server.py
GET  http://127.0.0.1:5066/health
POST http://127.0.0.1:5066/run
```

요청 요약:

```json
{
  "lang": "python",
  "code": "print(input()[::-1])",
  "stdin": "abc\n"
}
```

결과:

```text
health 200 {"ok": true, "service": "dongjun-judge", "docker": true, "uptimeSec": 0}
run 200 {"status": "OK", "stdout": "cba\n", "stderr": "", "durationMs": 472, "exitCode": 0}
```

판단:

- Docker runner 기반 custom input 실행이 실제로 동작합니다.

### 3-1. Judge 동시 실행 제한 health 확인

명령 요약:

```powershell
JUDGE_USE_DOCKER=1
JUDGE_PORT=5067
JUDGE_MAX_CONCURRENT_JOBS=2
python judge/server.py
GET http://127.0.0.1:5067/health
```

결과:

```text
200
{"ok": true, "service": "dongjun-judge", "docker": true, "maxConcurrentJobs": 2, "uptimeSec": 0}
```

판단:

- judge 서버가 동시 실행 제한 설정을 읽고 health 응답에 노출합니다.

### 4. Harness 테스트

명령:

```powershell
npm run harness:test
```

결과:

```text
Ran 5 tests in 2.126s
OK
```

### 5. Production build

명령:

```powershell
npm run build
```

결과 요약:

```text
✓ Compiled successfully
✓ Generating static pages (392/392)
/api/health dynamic route 추가 확인
```

### 6. E2E smoke

명령:

```powershell
npm run e2e
```

결과:

```text
2 passed
```

참고:

- Next dev server가 cross origin dev warning을 출력했습니다.
- 현재 테스트 실패 요인은 아니며, Phase 05/Nginx 배포 정리 때 dev origin 설정 또는 production 실행 기준으로 다시 다룹니다.

### 7. SQLite 백업

명령:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\backup-sqlite.ps1
```

결과:

```text
Backup created: .data\backups\dongjun-20260503-030359.db
```

판단:

- 로컬 SQLite 백업 스크립트가 정상 동작합니다.

## 예상 리스크

### 해소/정책 결정 완료

- Next.js 단일 프로세스 메모리 rate limit은 서버 재시작/다중 인스턴스에서 한계가 있습니다.
  - 정책: Phase 04에서는 단일 서버 운영 기준으로 in-memory rate limit을 사용합니다.
  - 확장 시점: Phase 06에서 Redis 기반 shared rate limit으로 교체합니다.
- Docker Desktop/WSL2가 준비되지 않으면 Docker runner 검증이 막힙니다.
  - 조치: 현재 Docker Desktop/WSL2 정상 동작을 확인했습니다.
- Docker runner의 `/work` tmpfs 권한 문제로 코드 복사가 실패할 수 있었습니다.
  - 조치: tmpfs mode를 조정했고 smoke test로 확인했습니다.

Phase 04 기준으로 남은 차단 리스크는 없습니다.
