# Phase 13 Batch 11: 핵심 알고리즘 20문제 확장

## 목표

이번 배치는 남은 확장 후보 중에서 exact compare 채점이 가능한 핵심 알고리즘 문제 20개를 추가했다. 그래프 탐색, 최단 경로, MST, DP, 이분 탐색, 조합/브루트포스 문제를 중심으로 구성했다.

모든 문제는 문제별 oracle 코드와 override 입력을 함께 추가했고, Python/C++ 사용자 제출이 같은 입력/출력 기준으로 채점될 수 있도록 구성했다.

## 추가 문제

- `brute_force-1025`
- `backtracking-1062`
- `binary_search-1166`
- `backtracking-1174`
- `graph_traversal-1240`
- `shortest_path-1261`
- `binary_search-1300`
- `backtracking-1342`
- `math-1359`
- `shortest_path-1389`
- `minimum_spanning_tree-1414`
- `dynamic_programming_1-1446`
- `dynamic_programming_1-1495`
- `shortest_path-1504`
- `dynamic_programming_1-1535`
- `binary_search-1561`
- `dynamic_programming_1-1577`
- `graph_traversal-1600`
- `shortest_path-1613`
- `dynamic_programming_2-1695`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-19.mjs
python scripts/verify-judge-overrides.py brute_force-1025 backtracking-1062 binary_search-1166 backtracking-1174 graph_traversal-1240 shortest_path-1261 binary_search-1300 backtracking-1342 math-1359 shortest_path-1389 minimum_spanning_tree-1414 dynamic_programming_1-1446 dynamic_programming_1-1495 shortest_path-1504 dynamic_programming_1-1535 binary_search-1561 dynamic_programming_1-1577 graph_traversal-1600 shortest_path-1613 dynamic_programming_2-1695
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 657개
- judge coverage: 657개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 현재 상태

- 이번 배치 처리: 20개
- 전체 앱 문제 수: 657개
- 확장 후보 기준 남은 문제: 347개

다음 배치도 20개 단위로 진행한다. 난도가 높거나 special judge가 필요한 문제는 exact compare 안정성이 확보되기 전까지 뒤로 미룬다.
