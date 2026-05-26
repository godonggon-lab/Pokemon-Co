# Phase 13 Batch 25 - Backtracking/Simulation Override 20개 추가

## 목표

남은 BOJ 확장 후보 중 exact compare가 안정적인 문제 20개를 추가한다. 경로 출력처럼 정답이 여러 개 가능한 문제는 뒤로 미루고, 숫자 또는 유일한 보드 상태가 출력되는 문제를 우선했다.

## 이번 배치 추가 문제

- `backtracking-1553`
- `backtracking-1799`
- `backtracking-1941`
- `graph_traversal-2151`
- `backtracking-2239`
- `shortest_path-2307`
- `simulation-2933`
- `trie-5446`
- `dynamic_programming_2-5624`
- `trie-9202`
- `backtracking-10597`
- `dynamic_programming_2-10653`
- `backtracking-12908`
- `simulation-15683`
- `simulation-16235`
- `simulation-17140`
- `simulation-17143`
- `simulation-17779`
- `simulation-17822`
- `simulation-20055`

## 작업 내용

- 각 문제별 `harness/overrides/*.py`에 edge/stress 입력을 추가했다.
- `scripts/import-expansion-manual-batch-33.mjs`로 20개 문제 metadata와 oracle 코드를 `data/problems-extra.json`에 반영했다.
- `backtracking-1941` oracle은 전체 25칸 조합 대신 S/Y 개수 기반 조합으로 줄여 자기검증 TLE를 제거했다.
- `trie-5446` oracle은 삭제 대상 하위 트리를 한 번에 지울 수 있도록 delete/keep propagation을 명확히 했다.
- `trie-9202` oracle은 빈 줄 유무에 흔들리지 않도록 non-empty line 기반으로 입력을 읽는다.

## 검증 결과

- `python scripts/verify-judge-overrides.py ...20개 slug...`: 통과
- `npm run data:map`: 통과, monster mapping 937개
- `npm run judge:coverage`: 통과, judgeReady 937개, missingCases 0개
- `npm run judge:lang-audit`: 통과, Python/C++ 제출 가능 경로 유지
- `npm run judge:audit`: 통과, missingCaseSlugs 없음
- `npx next build`: 통과, `/problem/[slug]` 937개 SSG 생성
- `npm run judge:docker-check`: 통과

## 현재 상태

- 총 override 수: 937개
- 남은 후보 수: 67개
- 다음 배치는 남은 simulation, shortest path, tree, DP 고난도 문제를 이어서 처리한다.
