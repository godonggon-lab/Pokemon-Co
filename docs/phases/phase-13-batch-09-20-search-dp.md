# Phase 13 Batch 09: 탐색/DP/이분탐색 20문제 확장

## 목표

이번 배치는 정답 출력이 고유한 탐색, DP, 이분탐색, 투포인터 문제 20개를 추가했다. 구성형 출력이나 special judge가 필요한 문제는 제외했다.

## 추가 문제

- `binary_search-7795` 먹을 것인가 먹힐 것인가
- `binary_search-8983` 사냥꾼
- `binary_search-9007` 카누 선수
- `two_pointer-10025` 게으른 백곰
- `brute_force-10472` 십자뒤집기
- `dynamic_programming_2-11054` 가장 긴 바이토닉 부분 수열
- `dynamic_programming_1-11060` 점프 점프
- `shortest_path-11403` 경로 찾기
- `shortest_path-11404` 플로이드
- `two_pointer-14921` 용액 합성하기
- `brute_force-15270` 친구 팰린드롬
- `dynamic_programming_1-15489` 파스칼 삼각형
- `dynamic_programming_2-15724` 주지수
- `binary_search-15810` 풍선 공장
- `brute_force-15970` 화살표 그리기
- `dynamic_programming_1-15988` 1, 2, 3 더하기 3
- `dynamic_programming_1-15992` 1, 2, 3 더하기 7
- `dynamic_programming_1-15993` 1, 2, 3 더하기 8
- `dynamic_programming_1-16194` 카드 구매하기 2
- `dynamic_programming_1-16195` 1, 2, 3 더하기 9

## 검증 결과

실행한 명령:

```bash
node scripts/import-expansion-manual-batch-17.mjs
python scripts/verify-judge-overrides.py binary_search-7795 binary_search-8983 binary_search-9007 two_pointer-10025 brute_force-10472 dynamic_programming_2-11054 dynamic_programming_1-11060 shortest_path-11403 shortest_path-11404 two_pointer-14921 brute_force-15270 dynamic_programming_1-15489 dynamic_programming_2-15724 binary_search-15810 brute_force-15970 dynamic_programming_1-15988 dynamic_programming_1-15992 dynamic_programming_1-15993 dynamic_programming_1-16194 dynamic_programming_1-16195
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

결과:

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 617개
- judge coverage: 617개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과
- Docker runner check: 통과

## 남은 작업량

- 확장 후보 파일 기준 남은 문제: 387개
- 다음 배치도 20개 단위로 처리하고, 배치 종료 시 commit/push한다.
