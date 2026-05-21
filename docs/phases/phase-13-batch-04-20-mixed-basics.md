# Phase 13 Batch 04: 기본 구현/브루트포스/DP 20문제 확장

## 목표

이번 배치는 남은 후보 중 출력 비교가 안정적인 정수/문자열 문제를 우선 추가했다. 부동소수 허용 오차가 필요한 문제는 아직 special judge 정책이 없으므로 제외했다.

## 추가 문제

- `dynamic_programming_1-1003` 피보나치 함수
- `brute_force-1018` 체스판 다시 칠하기
- `brute_force-1059` 좋은 구간
- `brute_force-1065` 한수
- `binary_search-1072` 게임
- `brute_force-1120` 문자열
- `dynamic_programming_1-1149` RGB거리
- `brute_force-1251` 단어 나누기
- `brute_force-1254` 팰린드롬 만들기
- `graph_traversal-1303` 전쟁 - 전투
- `dynamic_programming_1-1309` 동물원
- `greedy-1374` 강의실
- `brute_force-1411` 비슷한 단어
- `brute_force-1421` 나무꾼 이다솜
- `greedy-1474` 밑 줄
- `two_pointer-1484` 다이어트
- `brute_force-1487` 물건 팔기
- `brute_force-1503` 세 수 고르기
- `brute_force-1527` 금민수의 개수
- `brute_force-1543` 문서 검색

## 구현 내용

- `scripts/import-expansion-manual-batch-12.mjs`로 20문제 oracle을 등록했다.
- 각 문제별 `harness/overrides/*.py`를 추가했다.
- `brute_force-1503`은 naive 3중 전체 탐색이 oracle 실행에서 과하게 느려질 수 있어, 정답을 유지하면서 후보 `c`를 목표값 주변으로 좁혀 검증 속도를 안정화했다.

## 검증 결과

실행한 명령:

```bash
node scripts/import-expansion-manual-batch-12.mjs
python scripts/verify-judge-overrides.py dynamic_programming_1-1003 brute_force-1018 brute_force-1059 brute_force-1065 binary_search-1072 brute_force-1120 dynamic_programming_1-1149 brute_force-1251 brute_force-1254 graph_traversal-1303 dynamic_programming_1-1309 greedy-1374 brute_force-1411 brute_force-1421 greedy-1474 two_pointer-1484 brute_force-1487 brute_force-1503 brute_force-1527 brute_force-1543
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

결과:

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 517개
- judge coverage: 517개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

## 남은 작업량

- 확장 후보 파일 기준 남은 문제: 487개
- 다음 배치도 20개 단위로 처리하고, 배치 종료 시 commit/push한다.
