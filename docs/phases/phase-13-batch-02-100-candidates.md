# Phase 13 Batch 02. 100개 확장 후보

## 목표

포켓몬 1025종 목표를 향해 다음 편입 후보를 100개 단위로 크게 잡는다.

이 문서는 즉시 서비스 편입 목록이 아니라, 100개 후보를 작업 lane별로 나눈 실행 대기열이다.

## 선정 전략

1. 외부 Python/C++ 풀이가 있는 후보를 우선한다.
2. 이후 직접 oracle 작성이 쉬운 유형을 우선한다.
3. 같은 우선순위에서는 BOJ 번호가 낮은 문제를 먼저 둔다.

## 요약

- 후보 수: 100
- external_runtime: 6
- external_java_or_port: 13
- manual_oracle: 81

## 준비 상태

- needs_statement: 6
- needs_statement_and_oracle: 94

## 후보 목록

| # | BOJ | slug | lane | readiness | sample |
|---:|---|---|---|---|---:|
| 1 | 11663 | binary_search-11663 | external_runtime | needs_statement | 0 |
| 2 | 11728 | two_pointer-11728 | external_runtime | needs_statement | 0 |
| 3 | 17142 | graph_traversal-17142 | external_runtime | needs_statement | 0 |
| 4 | 1497 | backtracking-1497 | external_runtime | needs_statement | 0 |
| 5 | 14284 | shortest_path-14284 | external_runtime | needs_statement | 0 |
| 6 | 3025 | simulation-3025 | external_runtime | needs_statement | 0 |
| 7 | 12931 | greedy-12931 | external_java_or_port | needs_statement_and_oracle | 0 |
| 8 | 18234 | greedy-18234 | external_java_or_port | needs_statement_and_oracle | 0 |
| 9 | 1034 | brute_force-1034 | external_java_or_port | needs_statement_and_oracle | 0 |
| 10 | 21944 | data_structure2-21944 | external_java_or_port | needs_statement_and_oracle | 0 |
| 11 | 7453 | binary_search-7453 | external_java_or_port | needs_statement_and_oracle | 0 |
| 12 | 13422 | two_pointer-13422 | external_java_or_port | needs_statement_and_oracle | 0 |
| 13 | 2293 | dynamic_programming_1-2293 | external_java_or_port | needs_statement_and_oracle | 0 |
| 14 | 12026 | dynamic_programming_1-12026 | external_java_or_port | needs_statement_and_oracle | 0 |
| 15 | 18232 | graph_traversal-18232 | external_java_or_port | needs_statement_and_oracle | 0 |
| 16 | 1507 | shortest_path-1507 | external_java_or_port | needs_statement_and_oracle | 0 |
| 17 | 17396 | shortest_path-17396 | external_java_or_port | needs_statement_and_oracle | 0 |
| 18 | 20007 | shortest_path-20007 | external_java_or_port | needs_statement_and_oracle | 0 |
| 19 | 2637 | topological_sorting-2637 | external_java_or_port | needs_statement_and_oracle | 0 |
| 20 | 1213 | string-1213 | manual_oracle | needs_statement_and_oracle | 0 |
| 21 | 1622 | string-1622 | manual_oracle | needs_statement_and_oracle | 0 |
| 22 | 1718 | string-1718 | manual_oracle | needs_statement_and_oracle | 0 |
| 23 | 1942 | string-1942 | manual_oracle | needs_statement_and_oracle | 0 |
| 24 | 1972 | string-1972 | manual_oracle | needs_statement_and_oracle | 0 |
| 25 | 2115 | string-2115 | manual_oracle | needs_statement_and_oracle | 0 |
| 26 | 2671 | string-2671 | manual_oracle | needs_statement_and_oracle | 0 |
| 27 | 2852 | string-2852 | manual_oracle | needs_statement_and_oracle | 0 |
| 28 | 2941 | string-2941 | manual_oracle | needs_statement_and_oracle | 0 |
| 29 | 3005 | string-3005 | manual_oracle | needs_statement_and_oracle | 0 |
| 30 | 3107 | string-3107 | manual_oracle | needs_statement_and_oracle | 0 |
| 31 | 3613 | string-3613 | manual_oracle | needs_statement_and_oracle | 0 |
| 32 | 4446 | string-4446 | manual_oracle | needs_statement_and_oracle | 0 |
| 33 | 4836 | string-4836 | manual_oracle | needs_statement_and_oracle | 0 |
| 34 | 5534 | string-5534 | manual_oracle | needs_statement_and_oracle | 0 |
| 35 | 6996 | string-6996 | manual_oracle | needs_statement_and_oracle | 0 |
| 36 | 9242 | string-9242 | manual_oracle | needs_statement_and_oracle | 0 |
| 37 | 9536 | string-9536 | manual_oracle | needs_statement_and_oracle | 0 |
| 38 | 9933 | string-9933 | manual_oracle | needs_statement_and_oracle | 0 |
| 39 | 11478 | string-11478 | manual_oracle | needs_statement_and_oracle | 0 |
| 40 | 11655 | string-11655 | manual_oracle | needs_statement_and_oracle | 0 |
| 41 | 11656 | string-11656 | manual_oracle | needs_statement_and_oracle | 0 |
| 42 | 13022 | string-13022 | manual_oracle | needs_statement_and_oracle | 0 |
| 43 | 14405 | string-14405 | manual_oracle | needs_statement_and_oracle | 0 |
| 44 | 15927 | string-15927 | manual_oracle | needs_statement_and_oracle | 0 |
| 45 | 16890 | string-16890 | manual_oracle | needs_statement_and_oracle | 0 |
| 46 | 16916 | string-16916 | manual_oracle | needs_statement_and_oracle | 0 |
| 47 | 19583 | data_structure2-19583 | manual_oracle | needs_statement_and_oracle | 0 |
| 48 | 19844 | string-19844 | manual_oracle | needs_statement_and_oracle | 0 |
| 49 | 19948 | string-19948 | manual_oracle | needs_statement_and_oracle | 0 |
| 50 | 20114 | string-20114 | manual_oracle | needs_statement_and_oracle | 0 |
| 51 | 20210 | string-20210 | manual_oracle | needs_statement_and_oracle | 0 |
| 52 | 20944 | string-20944 | manual_oracle | needs_statement_and_oracle | 0 |
| 53 | 1188 | math-1188 | manual_oracle | needs_statement_and_oracle | 0 |
| 54 | 1456 | math-1456 | manual_oracle | needs_statement_and_oracle | 0 |
| 55 | 1669 | math-1669 | manual_oracle | needs_statement_and_oracle | 0 |
| 56 | 2168 | math-2168 | manual_oracle | needs_statement_and_oracle | 0 |
| 57 | 2436 | math-2436 | manual_oracle | needs_statement_and_oracle | 0 |
| 58 | 2553 | math-2553 | manual_oracle | needs_statement_and_oracle | 0 |
| 59 | 2824 | math-2824 | manual_oracle | needs_statement_and_oracle | 0 |
| 60 | 3343 | math-3343 | manual_oracle | needs_statement_and_oracle | 0 |
| 61 | 9421 | math-9421 | manual_oracle | needs_statement_and_oracle | 0 |
| 62 | 22943 | math-22943 | manual_oracle | needs_statement_and_oracle | 0 |
| 63 | 1022 | implementation-1022 | manual_oracle | needs_statement_and_oracle | 0 |
| 64 | 1283 | implementation-1283 | manual_oracle | needs_statement_and_oracle | 0 |
| 65 | 2469 | implementation-2469 | manual_oracle | needs_statement_and_oracle | 0 |
| 66 | 2877 | implementation-2877 | manual_oracle | needs_statement_and_oracle | 0 |
| 67 | 5766 | implementation-5766 | manual_oracle | needs_statement_and_oracle | 0 |
| 68 | 9081 | implementation-9081 | manual_oracle | needs_statement_and_oracle | 0 |
| 69 | 9934 | implementation-9934 | manual_oracle | needs_statement_and_oracle | 0 |
| 70 | 10703 | implementation-10703 | manual_oracle | needs_statement_and_oracle | 0 |
| 71 | 16719 | implementation-16719 | manual_oracle | needs_statement_and_oracle | 0 |
| 72 | 16927 | implementation-16927 | manual_oracle | needs_statement_and_oracle | 0 |
| 73 | 17128 | implementation-17128 | manual_oracle | needs_statement_and_oracle | 0 |
| 74 | 17276 | implementation-17276 | manual_oracle | needs_statement_and_oracle | 0 |
| 75 | 17406 | implementation-17406 | manual_oracle | needs_statement_and_oracle | 0 |
| 76 | 17470 | implementation-17470 | manual_oracle | needs_statement_and_oracle | 0 |
| 77 | 18311 | implementation-18311 | manual_oracle | needs_statement_and_oracle | 0 |
| 78 | 20164 | implementation-20164 | manual_oracle | needs_statement_and_oracle | 0 |
| 79 | 20327 | implementation-20327 | manual_oracle | needs_statement_and_oracle | 0 |
| 80 | 21277 | implementation-21277 | manual_oracle | needs_statement_and_oracle | 0 |
| 81 | 21611 | implementation-21611 | manual_oracle | needs_statement_and_oracle | 0 |
| 82 | 22858 | implementation-22858 | manual_oracle | needs_statement_and_oracle | 0 |
| 83 | 22859 | implementation-22859 | manual_oracle | needs_statement_and_oracle | 0 |
| 84 | 22860 | implementation-22860 | manual_oracle | needs_statement_and_oracle | 0 |
| 85 | 2571 | prefix_sum-2571 | manual_oracle | needs_statement_and_oracle | 0 |
| 86 | 2900 | prefix_sum-2900 | manual_oracle | needs_statement_and_oracle | 0 |
| 87 | 3673 | prefix_sum-3673 | manual_oracle | needs_statement_and_oracle | 0 |
| 88 | 5549 | prefix_sum-5549 | manual_oracle | needs_statement_and_oracle | 0 |
| 89 | 5875 | prefix_sum-5875 | manual_oracle | needs_statement_and_oracle | 0 |
| 90 | 10427 | prefix_sum-10427 | manual_oracle | needs_statement_and_oracle | 0 |
| 91 | 10713 | prefix_sum-10713 | manual_oracle | needs_statement_and_oracle | 0 |
| 92 | 14476 | prefix_sum-14476 | manual_oracle | needs_statement_and_oracle | 0 |
| 93 | 16139 | prefix_sum-16139 | manual_oracle | needs_statement_and_oracle | 0 |
| 94 | 16507 | prefix_sum-16507 | manual_oracle | needs_statement_and_oracle | 0 |
| 95 | 17123 | prefix_sum-17123 | manual_oracle | needs_statement_and_oracle | 0 |
| 96 | 17390 | prefix_sum-17390 | manual_oracle | needs_statement_and_oracle | 0 |
| 97 | 18866 | prefix_sum-18866 | manual_oracle | needs_statement_and_oracle | 0 |
| 98 | 19566 | prefix_sum-19566 | manual_oracle | needs_statement_and_oracle | 0 |
| 99 | 19951 | prefix_sum-19951 | manual_oracle | needs_statement_and_oracle | 0 |
| 100 | 20002 | dynamic_programming_2-20002 | manual_oracle | needs_statement_and_oracle | 0 |

## 실행 순서

1. `external_runtime` 중 statement가 있는 문제부터 10개 편입한다.
2. statement가 없는 문제는 `fetch-boj-statements.mjs --only=...`로 먼저 확보한다.
3. `manual_oracle`은 쉬운 유형부터 20개씩 oracle/override를 작성한다.
4. 각 묶음마다 `verify-judge-overrides`, `judge:coverage`, `next build`를 통과시킨다.

## 출력

- `data/problem-expansion-batch-02.json`

## 진행 로그

### 2026-05-16 수동 string 5문제 추가 편입

다음 문자열 문제 5개를 추가 편입했다.

- `string-1213` 팰린드롬 만들기
- `string-1718` 암호
- `string-2941` 크로아티아 알파벳
- `string-11655` ROT13
- `string-11656` 접미사 배열

검증:

- `python scripts/verify-judge-overrides.py string-1213 string-1718 string-2941 string-11655 string-11656`: 모두 AC
- `npm run judge:coverage`: 382개 전부 judge ready
- `npm run judge:lang-audit`: Python/C++ 제출 가능성 통과
- `npm run judge:audit`: missing case 0개
- `npx next build`: 통과

주의:

- 이번 실행에서 `npm run problems:expansion-audit`가 GitHub API rate limit 403으로 실패했다.
- 이 문서의 후보 목록은 다음 rate limit 해제 후 다시 생성해야 한다.
- 편입 완료된 문제 기준으로 앱의 확정 매핑 수는 382개다.

### 2026-05-16 수동 string 5문제 추가 편입 2

다음 문자열 문제 5개를 추가 편입했다.

- `string-9933` 민균이의 비밀번호
- `string-11478` 서로 다른 부분 문자열의 개수
- `string-14405` 피카츄
- `string-15927` 회문은 회문아니야!!
- `string-16916` 부분 문자열

검증:

- `python scripts/verify-judge-overrides.py string-9933 string-11478 string-14405 string-15927 string-16916`: 모두 AC
- `npm run judge:coverage`: 387개 전부 judge ready
- `npm run judge:lang-audit`: Python/C++ 제출 가능성 통과
- `npm run judge:audit`: missing case 0개
- `npx next build`: 통과

편입 완료된 문제 기준으로 앱의 확정 매핑 수는 387개다.

### 2026-05-16 수동 string 5문제 추가 편입 3

다음 문자열 문제 5개를 추가 편입했다.

- `string-1622` 공통 순열
- `string-1972` 놀라운 문자열
- `string-2671` 잠수함식별
- `string-2852` NBA 농구
- `string-3613` Java vs C++

검증:

- `python scripts/verify-judge-overrides.py string-1622 string-1972 string-2671 string-2852 string-3613`: 모두 AC
- `npm run judge:coverage`: 392개 전부 judge ready
- `npm run judge:lang-audit`: Python/C++ 제출 가능성 통과
- `npm run judge:audit`: missing case 0개
- `npx next build`: 통과

편입 완료된 문제 기준으로 앱의 확정 매핑 수는 392개다.

### 2026-05-16 수동 string 5문제 추가 편입 4

다음 문자열 문제 5개를 추가 편입했다.

- `string-5534` 간판
- `string-6996` 애너그램
- `string-9536` 여우는 어떻게 울지?
- `string-13022` 늑대와 올바른 단어
- `string-20944` 팰린드롬 척화비

함께 수정한 버그:

- `harness/judge_core.py`가 override의 dict 기반 `GeneratedCase`를 정식으로 해석하도록 수정했다.
- 이제 `input`, `kind`, `expected`가 있는 edge/stress/fuzz 케이스를 stdin 문자열로 오인하지 않는다.

검증:

- `python scripts/verify-judge-overrides.py string-5534 string-6996 string-9536 string-13022 string-20944`: 모두 AC
- `npm run judge:coverage`: 397개 전부 judge ready
- `npm run judge:lang-audit`: Python/C++ 제출 가능성 통과
- `npm run judge:audit`: missing case 0개
- `npx next build`: 통과

편입 완료된 문제 기준으로 앱의 확정 매핑 수는 397개다.

### 2026-05-18 수동 math 5문제 편입

다음 수학 문제 5개를 추가 편입했다.

- `math-1188` 음식 평론가
- `math-1456` 거의 소수
- `math-1669` 멍멍이 쓰다듬기
- `math-2168` 타일 위의 대각선
- `math-2436` 공약수

검증:

- `python scripts/verify-judge-overrides.py math-1188 math-1456 math-1669 math-2168 math-2436`: 모두 AC
- `npm run judge:coverage`: 402개 전부 judge ready
- `npm run judge:lang-audit`: Python/C++ 제출 가능성 통과
- `npm run judge:audit`: missing case 0개
- `npx next build`: 통과

편입 완료된 문제 기준으로 앱의 확정 매핑 수는 402개다.
