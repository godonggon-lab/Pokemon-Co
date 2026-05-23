# Phase 13 Batch 13: DP/그리디/위상정렬 20문제 확장

## 목표

이번 배치는 남은 확장 후보 중 DP, 그리디, 이분 탐색, 투 포인터, 위상 정렬 문제 20개를 추가했다. 출력이 고정되는 문제만 골라 exact compare 채점 안정성을 유지했다.

## 추가 문제

- `dynamic_programming_2-1727`
- `dynamic_programming_2-1757`
- `dynamic_programming_2-1823`
- `dynamic_programming_2-1958`
- `dynamic_programming_2-2073`
- `dynamic_programming_2-2157`
- `brute_force-2160`
- `dynamic_programming_2-2228`
- `dynamic_programming_2-2229`
- `dynamic_programming_2-2253`
- `greedy-2285`
- `binary_search-2412`
- `two_pointer-2428`
- `greedy-2457`
- `binary_search-2467`
- `backtracking-2529`
- `dynamic_programming_1-2565`
- `dynamic_programming_2-2616`
- `topological_sorting-2623`
- `dynamic_programming_2-2624`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-21.mjs
python scripts/verify-judge-overrides.py dynamic_programming_2-1727 dynamic_programming_2-1757 dynamic_programming_2-1823 dynamic_programming_2-1958 dynamic_programming_2-2073 dynamic_programming_2-2157 brute_force-2160 dynamic_programming_2-2228 dynamic_programming_2-2229 dynamic_programming_2-2253 greedy-2285 binary_search-2412 two_pointer-2428 greedy-2457 binary_search-2467 backtracking-2529 dynamic_programming_1-2565 dynamic_programming_2-2616 topological_sorting-2623 dynamic_programming_2-2624
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 697개
- judge coverage: 697개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 현재 상태

- 이번 배치 처리: 20개
- 전체 앱 문제 수: 697개
- 확장 후보 기준 남은 문제: 307개

Docker Desktop이 꺼져 있어 최초 Docker runner check는 실패했지만, Docker Desktop을 다시 시작한 뒤 동일 검증을 재실행해 통과했다.
