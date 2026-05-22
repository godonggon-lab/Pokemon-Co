# Phase 13 Batch 08: BFS/DP/이분탐색 20문제 확장

## 목표

이번 배치는 출력이 고유한 BFS, DP, 이분탐색, 브루트포스 문제 20개를 추가했다. 경로 출력처럼 여러 정답이 가능한 문제는 exact compare 채점 안정성을 위해 제외했다.

## 추가 문제

- `graph_traversal-11123` 양 한마리... 양 두마리...
- `brute_force-11170` 0의 개수
- `brute_force-11502` 세 개의 소수 문제
- `binary_search-11561` 징검다리
- `dynamic_programming_1-11568` 민균이의 계략
- `binary_search-11687` 팩토리얼 0의 개수
- `backtracking-12101` 1, 2, 3 더하기 2
- `graph_traversal-12761` 돌다리
- `graph_traversal-12851` 숨바꼭질 2
- `brute_force-12919` A와 B 2
- `dynamic_programming_2-13398` 연속합 2
- `binary_search-13702` 이상한 술집
- `brute_force-14225` 부분수열의 합
- `graph_traversal-14248` 점프 점프
- `brute_force-14501` 퇴사
- `binary_search-14575` 뒤풀이
- `binary_search-14627` 파닭파닭
- `brute_force-14912` 숫자 빈도수
- `two_pointer-15565` 귀여운 라이언
- `dynamic_programming_1-15624` 피보나치 수 7

## 검증 결과

실행한 명령:

```bash
node scripts/import-expansion-manual-batch-16.mjs
python scripts/verify-judge-overrides.py graph_traversal-11123 brute_force-11170 brute_force-11502 binary_search-11561 dynamic_programming_1-11568 binary_search-11687 backtracking-12101 graph_traversal-12761 graph_traversal-12851 brute_force-12919 dynamic_programming_2-13398 binary_search-13702 brute_force-14225 graph_traversal-14248 brute_force-14501 binary_search-14575 binary_search-14627 brute_force-14912 two_pointer-15565 dynamic_programming_1-15624
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

결과:

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 597개
- judge coverage: 597개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과
- Docker runner check: 통과

## 남은 작업량

- 확장 후보 파일 기준 남은 문제: 407개
- 다음 배치도 20개 단위로 처리하고, 배치 종료 시 commit/push한다.
