# DongJun 단일 서버 배포 예시

이 폴더는 Phase 05에서 사용하는 배포 설정 예시입니다.

- `nginx/dongjun.conf`: Nginx reverse proxy 예시
- `systemd/dongjun-web.service`: Next.js web 서비스 예시
- `systemd/dongjun-judge.service`: Python judge 서비스 예시

실제 서버에서는 `/opt/dongjun` 경로, Linux 사용자 이름, domain, Node/Python 경로를 서버 환경에 맞게 바꿔야 합니다.
