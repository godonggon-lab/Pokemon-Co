# Phase 06. 확장 구조 준비

## 목표

사용자가 늘어났을 때를 대비해 DB, 채점 worker, 큐, 캐시 구조로 확장할 수 있는 방향을 준비합니다.

## 범위

- SQLite에서 PostgreSQL로 이전하는 기준 정리
- migration 도구 검토
- Redis 기반 rate limit/queue 설계
- judge worker 분리 설계
- 제출 결과 polling 또는 SSE/WebSocket 설계
- 이미지/정적 데이터 캐싱 전략 정리

## 완료 기준

- 단일 서버 구조에서 다중 서버 구조로 넘어가는 판단 기준이 있다.
- DB migration 방향이 문서화되어 있다.
- judge queue/worker 구조의 책임 분리가 명확하다.

## 작업 로그

아직 시작 전입니다.

## 실행 결과(Output)

아직 실행 전입니다.

## 예상 리스크

- PostgreSQL 도입 시 기존 SQLite 데이터 이전 스크립트가 필요합니다.
- worker 분리 후에는 채점 결과 동기화 방식이 바뀌므로 UI/API 계약을 다시 잡아야 합니다.
