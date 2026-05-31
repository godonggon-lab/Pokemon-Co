# Phase 13 Batch 31 - Special Judge Override 5개 추가

## 목표

남은 후보 중 정답 출력이 하나로 고정되지 않는 문제를 처리하기 위해 harness에 문제별 checker 훅을 추가했다. 기존 exact compare 방식만 사용하면 맞는 출력도 오답 처리될 수 있으므로, 이번 배치에서는 사용자 출력이 문제 조건을 만족하는지 직접 검증한다.

## 추가한 문제

- `divide_and_conquer-14600`
- `divide_and_conquer-14601`
- `backtracking-15566`
- `simulation-15644`
- `divide_and_conquer-16438`

## 작업 내용

- `harness/generators.py`에 override별 `check_output(stdin, expected, actual)` 로더를 추가했다.
- `harness/judge_core.py`에서 checker가 있는 문제는 문자열 비교 대신 checker 결과로 AC/WA를 판단하도록 했다.
- `14600`, `14601`은 트로미노 타일 배치가 유효한지 검증한다.
- `15566`은 개구리 배치가 선호 연꽃과 통나무 대화 조건을 만족하는지 검증한다.
- `15644`는 최소 이동 횟수와 실제 경로가 구슬 탈출 조건을 만족하는지 검증한다.
- `16438`은 7일치 A/B 팀 배정에서 모든 원숭이 쌍이 최소 한 번 다른 팀이 되는지 검증한다.

## 검증 결과

- `python -m py_compile ...`: 통과
- `python scripts/verify-judge-overrides.py ...5개 slug...`: 통과
- `npm run data:map`: 통과, monster mapping 1009개
- `npm run judge:coverage`: 통과, judgeReady 1009개, missingCases 0개
- `npm run judge:lang-audit`: 통과, Python/C++ 제출 가능 경로 유지
- `npm run judge:audit`: 통과, missingCaseSlugs 없음
- `npm run judge:docker-check`: 통과
- `npx next build`: 통과, `/problem/[slug]` 1009개 SSG 생성
- `npm run problems:expansion-audit`: 통과, 남은 후보 1개

## 포켓몬 매핑 상태

이번 배치까지 총 1009개 문제가 `data/monster-map.json`에 매핑되어 있다. 이번에 추가한 5개 문제도 모두 포켓몬 매핑에 반영되었다.

## 남은 후보

- `brute_force-22947`

`22947`은 현재 확보 가능한 공개 단서로는 입력 형식과 oracle 의미를 확정하기 어렵다. 잘못 넣으면 judge 정확도를 해칠 수 있으므로 보류했다. 백준 원문 또는 검증 가능한 정답 풀이를 확보한 뒤 추가하는 것이 안전하다.
