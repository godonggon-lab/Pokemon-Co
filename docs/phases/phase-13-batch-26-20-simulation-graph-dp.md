# Phase 13 Batch 26 - Simulation/Graph/DP Override 20개 추가

## 목표

남은 후보 중 숫자 출력 또는 결정적인 경로 출력으로 검증 가능한 문제 20개를 추가한다. 다중 정답 가능성이 큰 문제는 피하고, 자기검증에서 입력 포맷과 시간 안정성을 먼저 확인했다.

## 이번 배치 추가 문제

- `shortest_path-11779`
- `brute_force-15728`
- `minimum_spanning_tree-17490`
- `simulation-17780`
- `simulation-17837`
- `simulation-19235`
- `simulation-19236`
- `simulation-19237`
- `simulation-19238`
- `backtracking-19942`
- `simulation-20056`
- `shortest_path-20168`
- `dynamic_programming_2-20181`
- `simulation-20665`
- `backtracking-20950`
- `topological_sorting-21276`
- `shortest_path-22865`
- `data_structure-22866`
- `graph_traversal-22868`
- `shortest_path-22870`

## 작업 내용

- 각 문제의 `harness/overrides/*.py`에 edge/stress 입력을 추가했다.
- `scripts/import-expansion-manual-batch-34.mjs`로 20개 문제 metadata와 oracle 코드를 `data/problems-extra.json`에 반영했다.
- `simulation-20665`는 입력 첫 줄을 `N T P` 형식으로 수정했다.
- `graph_traversal-22868`, `shortest_path-22870`은 왕복 경로가 존재하는 케이스로 교체했다.
- `simulation-17780`과 `simulation-17837`은 말 이동 규칙 차이를 분리해서 oracle을 작성했다.

## 검증 결과

- `python scripts/verify-judge-overrides.py ...20개 slug...`: 통과
- `npm run data:map`: 통과, monster mapping 957개
- `npm run judge:coverage`: 통과, judgeReady 957개, missingCases 0개
- `npm run judge:lang-audit`: 통과, Python/C++ 제출 가능 경로 유지
- `npm run judge:audit`: 통과, missingCaseSlugs 없음
- `npx next build`: 통과, `/problem/[slug]` 957개 SSG 생성
- `npm run judge:docker-check`: 통과

## 현재 상태

- 총 override 수: 957개
- 남은 후보 수: 47개
- 다음 배치는 남은 고난도 tree, backtracking, simulation, DP 문제를 이어서 처리한다.
