# Phase 12. 제출 기록 UI

## 목표

사용자가 자신의 최근 제출 결과를 프로필에서 확인할 수 있게 한다.

## 구현 내용

- SQLite `submissions` 테이블 조회 함수 추가:
  - `recentSubmissions(trainerId, limit)`
- `/api/trainer` 응답에 `submissions` 포함.
- `TrainerProvider`의 `TrainerProfile`에 `submissions` 추가.
- `/profile`에 최근 제출 테이블 추가.

## 표시 정보

```txt
문제
언어
결과
통과 케이스 수
첫 실패 case kind / verdict
실행 시간
제출 시간
```

## 저장 정책

- 코드 원문은 표시하지 않는다.
- 실패 케이스의 전체 input/output도 표시하지 않는다.
- DB에는 제출 요약, 코드 해시, 코드 크기만 저장한다.

## 검증 결과

```txt
npx tsc --noEmit
-> passed

npm run build
-> passed

npm run harness:test
-> OK, 14 tests

npm run judge:coverage
-> sampleOnly 0

npm run judge:quality
-> lowQualityCount 0
```
