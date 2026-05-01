# DongJun CodeDex 채점 인프라

## 빌드
```bash
cd judge
docker build -t dongjun-coderunner:latest .
```

## 실행 (개발)
```bash
# 1) 채점 서버 (호스트, 도커 데몬 접근 필요)
JUDGE_USE_DOCKER=1 python judge/server.py

# 2) Next.js dev
npm run dev
```

## 보안 가드
- 사용자 코드는 절대 호스트/Next 프로세스 안에서 실행되지 않음
- `--network=none` `--read-only` `--memory` `--pids-limit` `--ulimit nofile`
- `/work` 만 64m tmpfs, `/code` 는 RO 마운트
- 비루트 사용자(`runner`)로 실행
- 채점 서버는 `127.0.0.1` 바인딩만, 외부 노출 금지

## 환경변수
| 변수 | 기본값 | 설명 |
|---|---|---|
| `JUDGE_PORT` | `5050` | judge HTTP 포트 |
| `JUDGE_USE_DOCKER` | `1` | 0이면 LocalRunner (개발 전용, 위험) |
| `CODERUNNER_IMAGE` | `dongjun-coderunner:latest` | 사용자 코드 실행 이미지 |
| `JUDGE_URL` (Next) | `http://127.0.0.1:5050/judge` | 프론트→채점기 endpoint |
