# Phase 13 Batch 21: DP/그래프/DSU 20문제 확장

## 목표

이번 배치는 남은 확장 후보 중 숫자, 고정 문자열, 고정 형식 출력으로 채점할 수 있는 DP, 그래프 탐색, 분리 집합, 위상 정렬 문제 20개를 추가했다.
여러 유효한 출력이 가능한 문제는 exact compare에서 위험하므로 이번 배치에서 제외했다.

## 추가 문제

- `dynamic_programming_2-1082`
- `dynamic_programming_2-2629`
- `topological_sorting-9470`
- `graph_traversal-10711`
- `disjoint_set-11085`
- `binary_search-12757`
- `tree-14570`
- `topological_sorting-14676`
- `dynamic_programming_2-14863`
- `minimum_spanning_tree-14950`
- `graph_traversal-15558`
- `backtracking-15659`
- `graph_traversal-16973`
- `backtracking-16987`
- `disjoint_set-17398`
- `dynamic_programming_2-17404`
- `tree-19535`
- `topological_sorting-20119`
- `prefix_sum-20159`
- `binary_search-22871`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-29.mjs
python scripts/verify-judge-overrides.py dynamic_programming_2-1082 dynamic_programming_2-2629 topological_sorting-9470 graph_traversal-10711 disjoint_set-11085 binary_search-12757 tree-14570 topological_sorting-14676 dynamic_programming_2-14863 minimum_spanning_tree-14950 graph_traversal-15558 backtracking-15659 graph_traversal-16973 backtracking-16987 disjoint_set-17398 dynamic_programming_2-17404 tree-19535 topological_sorting-20119 prefix_sum-20159 binary_search-22871
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 문제 수: 857개
- judge coverage: 857개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 조정 사항

- 처음 선별 중 `graph_traversal-16956`은 이미 이전 배치에 들어간 문제였고, 여러 유효한 격자 출력이 가능한 문제라 이번 신규 배치에서는 제외했다. 기존 문제 데이터와 override는 원래 상태로 보존했다.
- `dynamic_programming_2-5569`까지 포함하면 배치가 21개가 되므로 이번 배치에서는 제외했다.
- Docker smoke test는 Java 단계에서 한 번 빈 출력으로 흔들렸지만, 재시도 로직이 적용된 상태에서 재실행 통과했다.

## 현재 상태

- 이번 배치 처리: 20개
- 전체 문제 수: 857개
- 확장 후보 기준 남은 문제: 147개
