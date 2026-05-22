# Phase 13 Batch 07: DP/문자열/기초 20문제 확장

## 목표

이번 배치는 출력 포맷이 명확하고 exact compare로 채점 가능한 DP, 문자열, 기초 구현 문제 20개를 추가했다.

## 추가 문제

- `brute_force-2635` 수 이어가기
- `dynamic_programming_2-2688` 줄어들지 않아
- `brute_force-3040` 백설 공주와 일곱 난쟁이
- `dynamic_programming_2-3067` Coins
- `dynamic_programming_2-4811` 알약
- `trie-5052` 전화번호 목록
- `simulation-5212` 지구 온난화
- `brute_force-5671` 호텔 방 번호
- `brute_force-5883` 아이폰 9S
- `divide_and_conquer-5904` Moo 게임
- `two_pointer-6159` Costume Party
- `tree-9372` 상근이의 여행
- `data_structure2-9375` 패션왕 신해빈
- `brute_force-9996` 한국이 그리울 땐 서버에 접속하지
- `dynamic_programming_1-10211` Maximum Subarray
- `brute_force-10448` 유레카 이론
- `dynamic_programming_1-10844` 쉬운 계단 수
- `dynamic_programming_1-11051` 이항 계수 2
- `dynamic_programming_1-11052` 카드 구매하기
- `dynamic_programming_1-11057` 오르막 수

## 검증 결과

실행한 명령:

```bash
node scripts/import-expansion-manual-batch-15.mjs
python scripts/verify-judge-overrides.py brute_force-2635 dynamic_programming_2-2688 brute_force-3040 dynamic_programming_2-3067 dynamic_programming_2-4811 trie-5052 simulation-5212 brute_force-5671 brute_force-5883 divide_and_conquer-5904 two_pointer-6159 tree-9372 data_structure2-9375 brute_force-9996 dynamic_programming_1-10211 brute_force-10448 dynamic_programming_1-10844 dynamic_programming_1-11051 dynamic_programming_1-11052 dynamic_programming_1-11057
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

결과:

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 577개
- judge coverage: 577개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과
- Docker runner check: 통과

## 남은 작업량

- 확장 후보 파일 기준 남은 문제: 427개
- 다음 배치도 20개 단위로 처리하고, 배치 종료 시 commit/push한다.
