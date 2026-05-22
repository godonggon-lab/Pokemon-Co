# Phase 13 Batch 06: Exact Compare 20문제 확장

## 목표

이번 배치는 정답 출력이 고유하고 exact compare로 안정적으로 채점 가능한 문제 20개를 추가했다. 위상정렬처럼 정답이 여러 개 가능한 문제는 이번 배치에서 제외했다.

## 추가 문제

- `brute_force-1548` 부분 삼각 수열
- `brute_force-1711` 직각삼각형
- `dynamic_programming_2-2225` 합분해
- `dynamic_programming_1-2302` 극장 좌석
- `brute_force-2304` 창고 다각형
- `binary_search-2343` 기타 레슨
- `brute_force-2435` 기상청 인턴 신현수
- `dynamic_programming_1-2491` 수열
- `two_pointer-2531` 회전 초밥
- `graph_traversal-2583` 영역 구하기
- `graph_traversal-2644` 촌수계산
- `binary_search-2792` 보석 상자
- `brute_force-2961` 도영이가 만든 맛있는 음식
- `brute_force-3085` 사탕 게임
- `graph_traversal-3184` 양
- `graph_traversal-3187` 양치기 꿍
- `two_pointer-3273` 두 수의 합
- `dynamic_programming_1-4097` 수익
- `graph_traversal-5014` 스타트링크
- `graph_traversal-5567` 결혼식

## 검증 결과

실행한 명령:

```bash
node scripts/import-expansion-manual-batch-14.mjs
python scripts/verify-judge-overrides.py brute_force-1548 brute_force-1711 dynamic_programming_2-2225 dynamic_programming_1-2302 brute_force-2304 binary_search-2343 brute_force-2435 dynamic_programming_1-2491 two_pointer-2531 graph_traversal-2583 graph_traversal-2644 binary_search-2792 brute_force-2961 brute_force-3085 graph_traversal-3184 graph_traversal-3187 two_pointer-3273 dynamic_programming_1-4097 graph_traversal-5014 graph_traversal-5567
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

결과:

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 557개
- judge coverage: 557개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

## 남은 작업량

- 확장 후보 파일 기준 남은 문제: 447개
- 다음 배치도 20개 단위로 처리하고, 배치 종료 시 commit/push한다.
