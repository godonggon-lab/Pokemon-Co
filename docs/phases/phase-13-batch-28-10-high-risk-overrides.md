# Phase 13 Batch 28 - High-risk Override 10개 추가

## 목표

남은 후보는 출력 형식이 복잡하거나 문제별 전용 로직이 강한 구간이다. 정확도를 우선하기 위해 이번 배치는 10개로 줄여 검증했다.

## 이번 배치 추가 문제

- `minimum_spanning_tree-1045`
- `dynamic_programming_2-1301`
- `backtracking-1469`
- `shortest_path-2211`
- `tree-2233`
- `divide_and_conquer-2374`
- `minimum_spanning_tree-2406`
- `backtracking-3165`
- `dynamic_programming_2-13902`
- `backtracking-15918`

## 작업 내용

- 각 문제의 `harness/overrides/*.py`에 edge/stress 입력을 추가했다.
- `scripts/import-expansion-manual-batch-36.mjs`로 10개 문제 metadata와 oracle 코드를 `data/problems-extra.json`에 반영했다.
- 경로/간선 목록 출력 문제는 tie가 적은 입력으로 구성해 exact compare 리스크를 줄였다.
- `minimum_spanning_tree-1045`, `minimum_spanning_tree-2406`은 추가 간선 선택 순서를 deterministic하게 만들었다.

## 검증 결과

- `python scripts/verify-judge-overrides.py ...10개 slug...`: 통과
- `npm run data:map`: 통과, monster mapping 987개
- `npm run judge:coverage`: 통과, judgeReady 987개, missingCases 0개
- `npm run judge:lang-audit`: 통과, Python/C++ 제출 가능 경로 유지
- `npm run judge:audit`: 통과, missingCaseSlugs 없음
- `npx next build`: 통과, `/problem/[slug]` 987개 SSG 생성
- `npm run judge:docker-check`: Docker Desktop 시작 후 통과

## 현재 상태

- 총 문제 수: 987개
- 총 override 수: 987개
- 남은 확장 후보 수: 23개
- 다음 배치는 남은 고난도 tree, DP, graph, simulation 문제를 계속 작은 단위로 처리한다.
