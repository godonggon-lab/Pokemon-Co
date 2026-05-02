# Phase 05. Nginx 기반 단일 서버 배포

## 목표

현재 로컬호스트 실행 구조를 서버 1대에서 운영 가능한 구조로 정리합니다. 외부 트래픽은 Nginx가 받고, Next.js와 judge는 내부 포트에만 바인딩합니다.

## 범위

- production 실행 방식 정리
- Nginx reverse proxy 설정 초안 작성
- systemd 또는 pm2 서비스 파일 초안 작성
- `.env.example` 작성
- 방화벽/포트 정책 정리
- HTTPS 적용 절차 정리
- judge 동시 실행 제한과 SQLite write 대기 설정 확인

## 완료 기준

- `npm run build` 후 `npm run start`로 실행 가능하다.
- Nginx가 `80/443`을 받고 Next.js `127.0.0.1:3000`으로 프록시한다.
- judge `127.0.0.1:5050`은 외부에 노출되지 않는다.
- 배포 절차를 문서만 보고 따라 할 수 있다.
- 배포 예시 파일이 `deploy/` 아래에 있다.

## 작업 로그

- Phase 04에서 만든 `.env.example`을 Phase 05 배포 기준으로 확장했다.
- judge 서버에 동시 실행 제한을 추가했다.
  - 환경변수: `JUDGE_MAX_CONCURRENT_JOBS`
  - 기본값: `3`
  - 환경변수: `JUDGE_JOB_ACQUIRE_TIMEOUT_S`
  - 기본값: `2.0`
- SQLite에 `busy_timeout = 5000`을 추가했다.
  - 여러 사용자의 write 요청이 겹칠 때 바로 실패하지 않고 최대 5초 대기한다.
- Nginx reverse proxy 예시를 추가했다.
  - `deploy/nginx/dongjun.conf`
- systemd 서비스 예시를 추가했다.
  - `deploy/systemd/dongjun-web.service`
  - `deploy/systemd/dongjun-judge.service`
- 배포 설정 설명 문서를 추가했다.
  - `deploy/README.md`

## 실행 결과(Output)

아직 실제 Linux 서버에 설치한 것은 아닙니다. 현재는 단일 서버 배포에 필요한 설정 파일과 절차를 준비했습니다.

추가된 파일:

```text
deploy/README.md
deploy/nginx/dongjun.conf
deploy/systemd/dongjun-web.service
deploy/systemd/dongjun-judge.service
```

로컬에서 계속 확인할 명령:

```powershell
npm run build
npm run harness:test
npm run e2e
docker build -t dongjun-coderunner:latest judge
```

현재 로컬 검증 결과:

```text
npm run build        OK
npm run start        OK (/api/health 200)
npm run harness:test OK
npm run e2e          OK
docker build         OK
```

주의:

- 처음에는 `npm run build`와 `npm run e2e`를 병렬로 돌려 `.next` 생성물이 충돌했습니다.
- `.next`를 삭제한 뒤 build와 e2e를 직렬 실행하니 정상 통과했습니다.
- `npm run e2e`는 dev server를 사용하므로 production start를 검증하려면 다시 `npm run build`를 실행한 뒤 `npm run start`를 확인해야 합니다.
- 배포/CI에서도 build와 dev server/e2e가 같은 `.next`를 동시에 만지지 않게 해야 합니다.

Production start 확인:

```text
GET http://127.0.0.1:3000/api/health
200
{"ok":true,"service":"dongjun-web","uptimeSec":0,"timestamp":"2026-05-02T18:35:20.293Z"}
```

Linux 서버 배포 시 권장 절차:

```bash
sudo useradd --system --create-home --home-dir /opt/dongjun --shell /usr/sbin/nologin dongjun
sudo usermod -aG docker dongjun
sudo mkdir -p /opt/dongjun
sudo chown -R dongjun:dongjun /opt/dongjun
```

앱 배치 후:

```bash
cd /opt/dongjun
npm ci
npm run build
docker build -t dongjun-coderunner:latest judge
cp .env.example .env
```

systemd 등록:

```bash
sudo cp deploy/systemd/dongjun-web.service /etc/systemd/system/
sudo cp deploy/systemd/dongjun-judge.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now dongjun-judge
sudo systemctl enable --now dongjun-web
```

Nginx 등록:

```bash
sudo cp deploy/nginx/dongjun.conf /etc/nginx/sites-available/dongjun
sudo ln -s /etc/nginx/sites-available/dongjun /etc/nginx/sites-enabled/dongjun
sudo nginx -t
sudo systemctl reload nginx
```

health check:

```bash
curl http://127.0.0.1:3000/api/health
curl http://127.0.0.1:5050/health
```

## 예상 리스크

- Windows 개발 환경과 Linux 운영 환경의 줄끝/권한 차이를 주의해야 합니다.
- Docker runner를 사용하는 judge 서버는 운영 서버에 Docker 권한이 필요합니다.
- `dongjun` 사용자를 `docker` 그룹에 넣으면 Docker socket 접근 권한을 갖게 됩니다. 장기적으로는 judge worker 분리나 rootless Docker를 검토합니다.
- Nginx HTTPS 인증서 설정은 실제 도메인이 필요하므로 서버 준비 후 Let's Encrypt로 진행합니다.
