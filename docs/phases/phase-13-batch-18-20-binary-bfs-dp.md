# Phase 13 Batch 18: 이분 탐색/BFS/DP 20문제 확장

## 목표

이번 배치는 확장 문제 중 exact compare로 안정적으로 채점할 수 있는 이분 탐색, 그래프 탐색, DP, 그리디, 분리 집합 문제 20개를 추가했다.
모든 override는 입력 생성과 정답 oracle을 함께 두어 Python/C++ 제출이 같은 입력/출력 기준으로 검증되도록 구성했다.

## 추가 문제

- `binary_search-16960`
- `tree-17073`
- `brute_force-17085`
- `graph_traversal-17086`
- `disjoint_set-17090`
- `binary_search-17124`
- `graph_traversal-17129`
- `binary_search-17179`
- `dynamic_programming_2-17208`
- `dynamic_programming_2-17265`
- `dynamic_programming_2-17845`
- `binary_search-17951`
- `binary_search-18113`
- `binary_search-18114`
- `brute_force-18868`
- `greedy-13019`
- `greedy-19539`
- `brute_force-19947`
- `disjoint_set-20040`
- `prefix_sum-20116`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-26.mjs
python scripts/verify-judge-overrides.py greedy-13019 binary_search-16960 tree-17073 brute_force-17085 graph_traversal-17086 disjoint_set-17090 binary_search-17124 graph_traversal-17129 binary_search-17179 dynamic_programming_2-17208 dynamic_programming_2-17265 dynamic_programming_2-17845 binary_search-17951 binary_search-18113 binary_search-18114 brute_force-18868 greedy-19539 brute_force-19947 disjoint_set-20040 prefix_sum-20116
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 문제 수: 797개
- judge coverage: 797개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 현재 상태

- 이번 배치 처리: 20개
- 전체 문제 수: 797개
- 확장 후보 기준 남은 문제: 207개

Docker runner check는 최초 실행에서 빈 stdout/stderr로 한 번 흔들렸지만, 재실행 결과 정상 통과했다. 현재 CI와 로컬 Docker 검증 모두 같은 runner 경로를 사용하므로, 이후에도 같은 증상이 반복되면 smoke test를 더 진단 가능한 형태로 보강한다.
