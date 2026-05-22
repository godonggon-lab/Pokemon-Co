# Phase 13 Batch 12: 고급 그래프/DP 20문제 확장

## 목표

이번 배치는 남은 후보 중에서 그래프, 트리, 최단 경로, 위상 정렬, DP, 백트래킹 문제 20개를 추가했다. 난도가 조금 올라간 문제들이지만 출력이 고정되어 있고, oracle로 기대 출력을 안정적으로 생성할 수 있는 문제만 골랐다.

## 추가 문제

- `tree-1167`
- `backtracking-1248`
- `divide_and_conquer-1493`
- `tree-1595`
- `shortest_path-1753`
- `shortest_path-1865`
- `dynamic_programming_2-1937`
- `binary_search-1939`
- `topological_sorting-1948`
- `shortest_path-1956`
- `backtracking-1987`
- `binary_search-2022`
- `backtracking-2023`
- `dynamic_programming_2-2056`
- `greedy-2109`
- `two_pointer-2118`
- `graph_traversal-2146`
- `shortest_path-2224`
- `topological_sorting-2252`
- `shortest_path-2458`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-20.mjs
python scripts/verify-judge-overrides.py tree-1167 backtracking-1248 divide_and_conquer-1493 tree-1595 shortest_path-1753 shortest_path-1865 dynamic_programming_2-1937 binary_search-1939 topological_sorting-1948 shortest_path-1956 backtracking-1987 binary_search-2022 backtracking-2023 dynamic_programming_2-2056 greedy-2109 two_pointer-2118 graph_traversal-2146 shortest_path-2224 topological_sorting-2252 shortest_path-2458
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 677개
- judge coverage: 677개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 현재 상태

- 이번 배치 처리: 20개
- 전체 앱 문제 수: 677개
- 확장 후보 기준 남은 문제: 327개

이번 배치에서 `backtracking-1248`은 self-judge 중 잘못된 stress 입력을 발견해 수정했다. 앞으로도 override 추가 시 self-judge를 먼저 통과시킨 뒤 전체 앱 검증으로 넘어간다.
