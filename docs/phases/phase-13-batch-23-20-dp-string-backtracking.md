# Phase 13 Batch 23: DP/문자열/백트래킹 20문제 확장

## 목표

이번 배치는 남은 확장 후보 중 문자열, DP, 백트래킹, 시뮬레이션 문제 20개를 추가했다.
모든 문제는 oracle 출력이 하나로 정해지는 형태로 구성했고, 여러 답이 가능한 출력 문제는 제외했다.

## 추가 문제

- `dynamic_programming_2-5569`
- `backtracking-6987`
- `string-2922`
- `graph_traversal-16432`
- `backtracking-16571`
- `backtracking-17136`
- `graph_traversal-17141`
- `data_structure2-17255`
- `trie-19585`
- `dynamic_programming_2-19645`
- `trie-20166`
- `backtracking-20208`
- `two_pointer-20442`
- `dynamic_programming_2-20542`
- `simulation-21922`
- `dynamic_programming_2-21925`
- `graph_traversal-21938`
- `dynamic_programming_2-21941`
- `brute_force-21943`
- `binary_search-22945`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-31.mjs
python scripts/verify-judge-overrides.py dynamic_programming_2-5569 backtracking-6987 string-2922 graph_traversal-16432 backtracking-16571 backtracking-17136 graph_traversal-17141 data_structure2-17255 trie-19585 dynamic_programming_2-19645 trie-20166 backtracking-20208 two_pointer-20442 dynamic_programming_2-20542 simulation-21922 dynamic_programming_2-21925 graph_traversal-21938 dynamic_programming_2-21941 brute_force-21943 binary_search-22945
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 문제 수: 897개
- judge coverage: 897개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 현재 상태

- 이번 배치 처리: 20개
- 전체 문제 수: 897개
- 확장 후보 기준 남은 문제: 107개
