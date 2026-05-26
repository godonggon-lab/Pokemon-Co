# Phase 13 Batch 16: 시뮬레이션/DSU/BFS 20문제 확장

## 목표

이번 배치는 남은 후보 중 exact compare가 안정적인 시뮬레이션, DSU, BFS, 트리, 투 포인터, 이분 탐색, 브루트포스 문제 20개를 추가했다. 구성 출력이나 여러 정답이 가능한 문제는 제외하고, oracle 출력이 하나로 고정되는 문제만 포함했다.

## 추가 문제

- `simulation-14594`
- `shortest_path-15723`
- `disjoint_set-15789`
- `two_pointer-15831`
- `tree-15900`
- `dynamic_programming_1-15991`
- `binary_search-16434`
- `tree-16437`
- `two_pointer-16472`
- `brute_force-16508`
- `binary_search-16564`
- `disjoint_set-16724`
- `backtracking-16922`
- `graph_traversal-16928`
- `graph_traversal-16932`
- `brute_force-16937`
- `backtracking-16938`
- `graph_traversal-16947`
- `graph_traversal-16948`
- `brute_force-16951`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-24.mjs
python scripts/verify-judge-overrides.py simulation-14594 shortest_path-15723 disjoint_set-15789 two_pointer-15831 tree-15900 dynamic_programming_1-15991 binary_search-16434 tree-16437 two_pointer-16472 brute_force-16508 binary_search-16564 disjoint_set-16724 backtracking-16922 graph_traversal-16928 graph_traversal-16932 brute_force-16937 backtracking-16938 graph_traversal-16947 graph_traversal-16948 brute_force-16951
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 757개
- judge coverage: 757개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 현재 상태

- 이번 배치 처리: 20개
- 전체 앱 문제 수: 757개
- 확장 후보 기준 남은 문제: 247개

이번 배치부터는 남은 후보 중 구성 출력, 특수 judge 성격, 매우 큰 구현량의 문제 비중이 커지고 있어, 계속 exact compare 안정성을 우선해서 선별한다.
