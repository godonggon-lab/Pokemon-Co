# Phase 13 Batch 14: BFS/DP/백트래킹 20문제 확장

## 목표

이번 배치는 남은 후보 중 exact compare 채점이 가능한 BFS, DP, 트리, DSU, 백트래킹 문제 20개를 추가했다. 출력 형식이 민감한 문제도 포함되어 있어 override self-judge로 빈 줄과 순서까지 확인했다.

## 추가 문제

- `dynamic_programming_1-1633`
- `binary_search-2121`
- `shortest_path-2660`
- `backtracking-2661`
- `graph_traversal-2665`
- `graph_traversal-2668`
- `binary_search-2866`
- `graph_traversal-3055`
- `backtracking-3980`
- `tree-4803`
- `graph_traversal-5427`
- `dynamic_programming_2-5582`
- `tree-5639`
- `backtracking-6443`
- `backtracking-6603`
- `backtracking-7490`
- `disjoint_set-7511`
- `graph_traversal-9019`
- `shortest_path-10159`
- `dynamic_programming_2-10942`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-22.mjs
python scripts/verify-judge-overrides.py dynamic_programming_1-1633 binary_search-2121 shortest_path-2660 backtracking-2661 graph_traversal-2665 graph_traversal-2668 binary_search-2866 graph_traversal-3055 backtracking-3980 tree-4803 graph_traversal-5427 dynamic_programming_2-5582 tree-5639 backtracking-6443 backtracking-6603 backtracking-7490 disjoint_set-7511 graph_traversal-9019 shortest_path-10159 dynamic_programming_2-10942
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 717개
- judge coverage: 717개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 현재 상태

- 이번 배치 처리: 20개
- 전체 앱 문제 수: 717개
- 확장 후보 기준 남은 문제: 287개

`backtracking-3980`은 최초 stress 케이스가 지나치게 넓어 oracle 검증 시간이 길어졌기 때문에, 시간 안에 끝나면서도 분기를 검증하는 sparse 케이스로 조정했다.
