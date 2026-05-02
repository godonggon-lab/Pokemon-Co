# DongJun CodeDex 단계별 개발 기록

이 폴더는 `docs/future-development-plan.md`의 내용을 실제 개발 단계로 쪼개어 관리하기 위한 공간입니다.

각 phase 문서는 다음 형식을 따릅니다.

- 목표: 이 단계에서 해결하려는 문제
- 범위: 이번 단계에 포함되는 작업
- 완료 기준: 끝났다고 판단할 수 있는 조건
- 작업 로그: 실제로 진행한 내용
- 실행 결과(Output): 실행한 명령, 확인 결과, 실패/보류 사유

## 전체 Phase

| Phase | 문서 | 핵심 목표 | 상태 |
|---|---|---|---|
| 00 | [phase-00-baseline.md](./phase-00-baseline.md) | 현재 상태 점검, 작업 규칙, 검증 기준 만들기 | 완료 |
| 01 | [phase-01-korean-encoding-and-copy.md](./phase-01-korean-encoding-and-copy.md) | 한글/UTF-8 상태 검증과 편집 규칙 추가 | 완료 |
| 02 | [phase-02-judge-reliability.md](./phase-02-judge-reliability.md) | sample/fuzz 기반 채점 신뢰도 개선 | 완료 |
| 03 | [phase-03-playground-ux.md](./phase-03-playground-ux.md) | 코드 자동 저장, custom input 실행, 제출 단축키 | 완료 |
| 04 | [phase-04-security-and-ops.md](./phase-04-security-and-ops.md) | rate limit, health check, Docker runner, 백업 | 완료 |
| 05 | [phase-05-nginx-deploy.md](./phase-05-nginx-deploy.md) | Nginx/systemd 단일 서버 배포 준비 | 완료 |
| 06 | [phase-06-scale-up.md](./phase-06-scale-up.md) | PostgreSQL, 큐, worker 분리 등 확장 설계 | 예정 |

## 진행 원칙

1. 한 phase 안에서 너무 많은 것을 고치지 않는다.
2. phase마다 코드 변경과 검증 결과를 문서에 남긴다.
3. 실패한 명령도 숨기지 않고 남긴다. 실패 원인과 다음 행동이 더 중요하다.
4. 배포/보안/채점 관련 변경은 반드시 검증 명령을 함께 기록한다.
5. 사용자가 읽었을 때 “무엇을 왜 했는지” 이해할 수 있게 한국어로 작성한다.
