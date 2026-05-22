# Phase 13 Batch 10: 그래프/DP/탐색 20문제 확장

## 목표

이번 배치는 포켓몬 도감 확장 후보 중에서 정답 출력이 고정되어 있고, exact compare 채점으로 안정적으로 다룰 수 있는 그래프 탐색, 최단 경로, DP, 이분 탐색, 투 포인터 문제 20개를 추가했다.

구성 출력처럼 여러 정답이 가능한 문제는 제외하고, Python/C++ 제출 모두 같은 입력과 출력 기준으로 검증될 수 있는 문제만 포함했다.

## 추가 문제

- `dynamic_programming_1-2670`
- `dynamic_programming_2-2758`
- `dynamic_programming_1-2876`
- `binary_search-3020`
- `two_pointer-3151`
- `dynamic_programming_2-4095`
- `shortest_path-4485`
- `shortest_path-5972`
- `graph_traversal-6118`
- `two_pointer-6137`
- `binary_search-6209`
- `graph_traversal-7562`
- `dynamic_programming_2-9084`
- `shortest_path-9205`
- `graph_traversal-9466`
- `graph_traversal-10026`
- `graph_traversal-11559`
- `data_structure2-12764`
- `greedy-13975`
- `binary_search-16401`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-18.mjs
python scripts/verify-judge-overrides.py dynamic_programming_1-2670 dynamic_programming_2-2758 dynamic_programming_1-2876 binary_search-3020 two_pointer-3151 dynamic_programming_2-4095 shortest_path-4485 shortest_path-5972 graph_traversal-6118 two_pointer-6137 binary_search-6209 graph_traversal-7562 dynamic_programming_2-9084 shortest_path-9205 graph_traversal-9466 graph_traversal-10026 graph_traversal-11559 data_structure2-12764 greedy-13975 binary_search-16401
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 637개
- judge coverage: 637개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 현재 상태

- 이번 배치 처리: 20개
- 전체 앱 문제 수: 637개
- 확장 후보 기준 남은 문제: 367개

다음 배치도 같은 기준으로 20개씩 처리한다. 특히 judge 핵심 품질을 위해 override는 문제별 deterministic oracle과 입력 생성기를 함께 유지한다.
