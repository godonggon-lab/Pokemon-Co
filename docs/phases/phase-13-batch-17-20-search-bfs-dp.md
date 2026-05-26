# Phase 13 Batch 17: 탐색/DP/이분탐색 20문제 확장

## 목표

이번 배치는 남은 후보 중 exact compare가 안정적인 이분 탐색, DP, BFS, 최단 경로, 브루트포스 문제 20개를 추가했다. 출력이 하나로 고정되는 문제만 포함했고, 구성 출력이나 여러 정답이 가능한 문제는 제외했다.

## 추가 문제

- `binary_search-15732`
- `binary_search-15823`
- `dynamic_programming_1-17175`
- `dynamic_programming_1-17212`
- `binary_search-17266`
- `dynamic_programming_1-17291`
- `binary_search-17393`
- `binary_search-17451`
- `binary_search-17503`
- `brute_force-17521`
- `brute_force-17610`
- `graph_traversal-17616`
- `shortest_path-18223`
- `shortest_path-18243`
- `graph_traversal-18352`
- `dynamic_programming_1-18353`
- `graph_traversal-18404`
- `graph_traversal-18405`
- `backtracking-18429`
- `brute_force-18512`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-25.mjs
python scripts/verify-judge-overrides.py binary_search-15732 binary_search-15823 dynamic_programming_1-17175 dynamic_programming_1-17212 binary_search-17266 dynamic_programming_1-17291 binary_search-17393 binary_search-17451 binary_search-17503 brute_force-17521 brute_force-17610 graph_traversal-17616 shortest_path-18223 shortest_path-18243 graph_traversal-18352 dynamic_programming_1-18353 graph_traversal-18404 graph_traversal-18405 backtracking-18429 brute_force-18512
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 777개
- judge coverage: 777개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 현재 상태

- 이번 배치 처리: 20개
- 전체 앱 문제 수: 777개
- 확장 후보 기준 남은 문제: 227개

`binary_search-17503` oracle에서 generator expression 괄호 누락이 self-judge에서 발견되어 수정했다. 또한 Docker smoke test에서 C++/Java 컴파일 시간이 2초를 넘는 환경이 있어, 설치/실행 확인용 체크 스크립트의 C++/Java 제한 시간을 15초로 조정했다.
