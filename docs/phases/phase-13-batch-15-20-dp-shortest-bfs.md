# Phase 13 Batch 15: DP/최단경로/BFS 20문제 확장

## 목표

이번 배치는 남은 후보 중 exact compare 채점이 안정적인 DP, 최단 경로, BFS, 트리, DSU, 트라이 문제 20개를 추가했다. 경로 출력처럼 여러 정답이 가능한 문제는 제외하고, 기대 출력이 하나로 고정되는 문제만 포함했다.

## 추가 문제

- `dynamic_programming_2-11049`
- `dynamic_programming_2-11066`
- `shortest_path-11265`
- `shortest_path-11562`
- `shortest_path-11657`
- `dynamic_programming_2-12865`
- `dynamic_programming_2-13302`
- `binary_search-13397`
- `shortest_path-13424`
- `graph_traversal-13565`
- `dynamic_programming_2-14226`
- `tree-14267`
- `dynamic_programming_1-14430`
- `graph_traversal-14442`
- `graph_traversal-14496`
- `disjoint_set-14595`
- `tree-14675`
- `dynamic_programming_2-14699`
- `trie-14725`
- `dynamic_programming_2-14728`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-23.mjs
python scripts/verify-judge-overrides.py dynamic_programming_2-11049 dynamic_programming_2-11066 shortest_path-11265 shortest_path-11562 shortest_path-11657 dynamic_programming_2-12865 dynamic_programming_2-13302 binary_search-13397 shortest_path-13424 graph_traversal-13565 dynamic_programming_2-14226 tree-14267 dynamic_programming_1-14430 graph_traversal-14442 graph_traversal-14496 disjoint_set-14595 tree-14675 dynamic_programming_2-14699 trie-14725 dynamic_programming_2-14728
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 737개
- judge coverage: 737개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 현재 상태

- 이번 배치 처리: 20개
- 전체 앱 문제 수: 737개
- 확장 후보 기준 남은 문제: 267개

처음에는 21개가 선택되어 `simulation-14594`를 다음 배치로 넘겼다. Docker Desktop이 꺼져 있어 최초 Docker runner check는 실패했지만, Docker Desktop을 다시 시작한 뒤 재실행해 통과했다.
