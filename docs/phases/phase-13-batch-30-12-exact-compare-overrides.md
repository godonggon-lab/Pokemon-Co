# Phase 13 Batch 30 - Exact Compare Override 12개 추가

## 목표

남은 확장 후보 중 출력이 숫자 또는 `true/false`처럼 exact compare로 안전한 문제를 먼저 처리했다. 다중 정답 출력이나 출력 형식 자유도가 큰 문제는 현재 harness의 문자열 비교 방식으로는 오답 판정 위험이 있으므로 이번 배치에서 제외했다.

## 추가한 문제

- `backtracking-1729`
- `dynamic_programming_on_trees-2058`
- `tree-4315`
- `tree-4933`
- `backtracking-10421`
- `tree-12912`
- `dynamic_programming_on_trees-12978`
- `dynamic_programming_2-14945`
- `brute_force-15779`
- `dynamic_programming_1-20162`
- `dynamic_programming_2-20667`
- `two_pointer-21279`

## 작업 내용

- 각 문제에 `harness/overrides/*.py` 입력 케이스를 추가했다.
- `scripts/import-expansion-manual-batch-38.mjs`로 metadata와 Python oracle을 추가했다.
- tree/DP 문제는 작은 edge case와 구조가 갈리는 stress case를 나누어 넣었다.
- `two_pointer-21279`는 override 입력이 작기 때문에 oracle은 좌표 후보를 완전 탐색해 정답을 계산한다.

## 검증 결과

- `python scripts/verify-judge-overrides.py ...12개 slug...`: 통과
- `npm run data:map`: 통과, monster mapping 1004개
- `npm run judge:coverage`: 통과, judgeReady 1004개, missingCases 0개
- `npm run judge:lang-audit`: 통과, Python/C++ 제출 가능 경로 유지
- `npm run judge:audit`: 통과, missingCaseSlugs 없음
- `npm run judge:docker-check`: 통과
- `npx next build`: 통과, `/problem/[slug]` 1004개 SSG 생성
- `npm run problems:expansion-audit`: 통과, 남은 후보 6개

## 남은 후보

- `divide_and_conquer-14600`
- `divide_and_conquer-14601`
- `backtracking-15566`
- `simulation-15644`
- `divide_and_conquer-16438`
- `brute_force-22947`

`14600`, `14601`, `15566`, `15644`, `16438`은 정답이 여러 개 가능한 출력 생성형 문제라 special judge/checker 지원이 먼저 필요하다. `22947`은 현재 확보한 외부 단서만으로 입력 의미와 oracle을 확정하기 어려워 보류했다.

## 포켓몬 매핑 상태

이번 배치까지 `npm run data:map` 기준 총 1004개 문제가 포켓몬에 매핑되어 있다. 즉 이번에 추가한 12개 문제도 모두 `data/monster-map.json`에 반영되었다.
