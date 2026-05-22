# Phase 13 Batch 05: DP/자료구조/그래프 20문제 확장

## 목표

이번 배치는 남은 후보 중 DP, 자료구조, 그래프 탐색, 최단거리 문제를 섞어서 20개 추가했다. 모두 입력/출력 exact compare로 검증 가능한 문제이며, special judge나 부동소수 허용 오차는 필요하지 않다.

## 추가 문제

- `two_pointer-1644` 소수의 연속합
- `data_structure2-1655` 가운데를 말해요
- `dynamic_programming_1-1660` 캡틴 이다솜
- `brute_force-1668` 트로피 진열
- `dynamic_programming_1-1699` 제곱수의 합
- `simulation-1713` 후보 추천하기
- `graph_traversal-1743` 음식물 피하기
- `backtracking-1759` 암호 만들기
- `topological_sorting-1766` 문제집
- `divide_and_conquer-1780` 종이의 개수
- `data_structure-1863` 스카이라인 쉬운거
- `brute_force-1895` 필터
- `dynamic_programming_2-1915` 가장 큰 정사각형
- `shortest_path-1916` 최소비용 구하기
- `graph_traversal-1926` 그림
- `dynamic_programming_1-1932` 정수 삼각형
- `dynamic_programming_1-1965` 상자넣기
- `two_pointer-2003` 수들의 합 2
- `dynamic_programming_1-2011` 암호코드
- `dynamic_programming_1-2193` 이친수

## 검증 결과

실행한 명령:

```bash
node scripts/import-expansion-manual-batch-13.mjs
python scripts/verify-judge-overrides.py two_pointer-1644 data_structure2-1655 dynamic_programming_1-1660 brute_force-1668 dynamic_programming_1-1699 simulation-1713 graph_traversal-1743 backtracking-1759 topological_sorting-1766 divide_and_conquer-1780 data_structure-1863 brute_force-1895 dynamic_programming_2-1915 shortest_path-1916 graph_traversal-1926 dynamic_programming_1-1932 dynamic_programming_1-1965 two_pointer-2003 dynamic_programming_1-2011 dynamic_programming_1-2193
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

결과:

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 537개
- judge coverage: 537개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

## 남은 작업량

- 확장 후보 파일 기준 남은 문제: 467개
- 다음 배치도 20개 단위로 처리하고, 배치 종료 시 commit/push한다.
