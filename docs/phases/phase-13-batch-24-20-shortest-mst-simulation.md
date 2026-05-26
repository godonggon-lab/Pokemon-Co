# Phase 13 Batch 24 - Shortest/MST/Simulation Override 20개 추가

## 목표

남은 문제 override를 20개 단위로 확장하면서, 문제별 입력 안정성과 oracle 자기검증을 유지한다.

## 이번 배치 추가 문제

- `divide_and_conquer-1030`
- `shortest_path-1219`
- `shortest_path-1277`
- `shortest_path-1445`
- `minimum_spanning_tree-1944`
- `graph_traversal-2194`
- `tree-2263`
- `shortest_path-2982`
- `shortest_path-9370`
- `graph_traversal-14923`
- `shortest_path-16118`
- `minimum_spanning_tree-16202`
- `graph_traversal-16985`
- `dynamic_programming_2-17216`
- `minimum_spanning_tree-17472`
- `minimum_spanning_tree-18769`
- `shortest_path-20182`
- `shortest_path-20183`
- `simulation-21609`
- `shortest_path-21940`

## 작업 내용

- 각 문제의 `harness/overrides/*.py`에 edge/stress 입력을 추가했다.
- `scripts/import-expansion-manual-batch-32.mjs`로 20개 문제 metadata와 oracle 코드를 `data/problems-extra.json`에 반영했다.
- `shortest_path-2982`의 경로 입력 순서를 BOJ 입력 포맷에 맞게 수정했다.
- `graph_traversal-16985` oracle은 최단 가능 거리 12 발견 시 즉시 종료하도록 최적화했다.
- `minimum_spanning_tree-17472` oracle은 섬 라벨링에서 방문 배열을 사용하도록 수정했다.

## 검증 결과

- `python scripts/verify-judge-overrides.py ...20개 slug...`: 통과
- `npm run data:map`: 통과, monster mapping 917개
- `npm run judge:coverage`: 통과, judgeReady 917개, missingCases 0개
- `npm run judge:lang-audit`: 통과, Python/C++ 제출 가능 경로 유지
- `npm run judge:audit`: 통과, missingCaseSlugs 없음
- `npx next build`: 통과, `/problem/[slug]` 917개 SSG 생성
- `npm run judge:docker-check`: 통과

## 현재 상태

- 총 override 수: 917개
- 남은 후보 수: 87개
- 다음 배치는 남은 고난도 backtracking, simulation, shortest path, tree 계열을 이어서 처리한다.
