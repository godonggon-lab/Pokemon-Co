# Phase 13. 포켓몬 도감 문제 확장

## 목표

전국도감 1025종에 맞춰 앱의 문제 수를 1025개까지 확장한다. 현재 앱은 slug 기준 362문제를 서비스하고 있지만, BOJ 번호 unique 기준으로는 353문제다. 포켓몬 1종당 문제 1개를 목표로 하므로 unique 문제 기준 추가 672문제를 단계적으로 확보한다.

## 기본 원칙

- 문제 수 기준은 `카테고리-문제 조합`이 아니라 BOJ 문제 번호 기준 unique 문제로 잡는다.
- 문제 본문은 원문을 그대로 복제하지 않고, 앱 컨셉에 맞춘 요약/재작성과 원문 링크로 관리한다.
- 채점 가능한 문제만 서비스에 편입한다.
- 정답 코드만 있는 상태는 충분하지 않다. sample, edge, fuzz, 필요 시 stress case까지 있어야 한다.
- 난이도는 solved.ac 기준 `bronze`, `silver`, `gold`, `platinum`으로 접는다.
- 포켓몬 매핑은 기존 규칙을 유지한다.
  - bronze: 진화 전
  - silver: 1단계 진화
  - gold: 2단계 진화
  - platinum: 전설/환상

## Phase 분할

### 13-A. 후보 목록 감사

`godonggon-lab/baekjoon`의 `algorithms/*/list.md`를 읽어서 전체 후보를 만든다.

완료 기준:

- 현재 앱에 있는 문제 수를 계산한다.
- `algorithms/list.md` 기준 unique BOJ 문제 수를 계산한다.
- 앱에 없는 후보를 산출한다.
- 각 후보를 다음 상태로 분류한다.
  - `repo_solution_ready`: 같은 레포의 `solution/`에 코드가 있음
  - `external_solution_candidate`: list에 외부 풀이 링크가 있음
  - `needs_oracle`: 정답/oracle을 직접 확보해야 함

출력:

- `data/problem-expansion-candidates.json`
- `docs/problem-expansion-audit.md`

명령:

```bash
npm run problems:expansion-audit
```

### 13-B. solved.ac 난이도 보강

후보 문제의 solved.ac 레벨을 수집해 4개 티어로 접는다.

완료 기준:

- 추가 663개 후보 중 난이도 unknown을 최소화한다.
- bronze/silver/gold/platinum 분포를 확인한다.
- 플래티넘 후보가 부족하면 gold 상위 문제를 임시 대체하지 않고, 플래티넘 후보 수집을 별도 이슈로 분리한다.

### 13-C. 문제 본문 확보

BOJ 원문 복제 대신 앱용 설명을 작성한다.

완료 기준:

- 문제 제목, 번호, 링크, 입력/출력 요약, 예제 입출력, 제한 정보를 저장한다.
- 본문은 직접 요약하거나 포켓몬 컨셉에 맞춰 재작성한다.
- 원문 확인용 BOJ 링크를 유지한다.

### 13-D. 정답/oracle 확보

후보를 안전한 순서로 편입한다.

우선순위:

1. `repo_solution_ready`
2. `external_solution_candidate`
3. `needs_oracle` 중 입출력/수학/문자열/단순 구현
4. 그래프/DP/시뮬레이션
5. special judge 필요 문제

완료 기준:

- Python 또는 C++ 기준 oracle이 있다.
- sample case가 있다.
- edge/fuzz case가 있다.
- 시간 초과를 잡아야 하는 문제는 stress case가 있다.

### 13-E. 100개 단위 편입

한 번에 663개를 넣지 않고 100개 단위로 서비스에 넣는다.

완료 기준:

- 각 batch마다 `npm run judge:coverage`
- 각 batch마다 `npm run judge:verify-overrides`
- 각 batch마다 `npm run data:map`
- 앱 빌드 성공

## 현재 실행 결과

13-A 후보 감사와 13-B solved.ac 보강 시도를 시작했다.

### 2026-05-14 실행 로그

명령:

```bash
npm run problems:expansion-audit
```

결과:

- 현재 앱 문제 수: 353개 unique BOJ 문제
- 목표 문제 수: 1025개
- 추가 필요 문제 수: 672개
- `algorithms/list.md` 기준 unique 후보: 993개
- 현재 앱에 없는 후보: 642개
- 1차 도감 편입 후보: 642개
- 목표 대비 부족분: 30개
- 후보 상태:
  - `external_solution_candidate`: 29개
  - `needs_oracle`: 613개
  - `repo_solution_ready`: 0개

명령:

```bash
npm run problems:expansion-solvedac
```

결과:

- solved.ac API가 현재 로컬 실행 환경에서 Cloudflare 403을 반환했다.
- 따라서 후보 642개의 난이도는 아직 `unknown` 상태다.
- 스크립트는 실패를 `data/problem-expansion-candidates.json`의 `solvedAcFailures`에 기록하고 종료한다.

출력:

- `data/problem-expansion-candidates.json`
- `docs/problem-expansion-audit.md`

## 다음 작업

1. solved.ac 난이도 수집 우회 방법을 정한다.
   - GitHub Actions에서 실행해 통과하는지 확인
   - 브라우저 기반 수집으로 전환
   - 수동 CSV 업로드 방식 지원
2. 부족한 30개 후보를 추가 확보한다.
   - solved.ac 태그별 검색
   - 현재 알고리즘 분류와 맞는 쉬운 문제 우선
3. `external_solution_candidate` 29개를 먼저 검토한다.
4. `needs_oracle` 중 bronze/silver로 예상되는 입출력/수학/문자열 문제를 1차 batch로 묶는다.
5. 1차 100문제 편입 계획을 별도 문서로 만든다.

### 2026-05-14 추가 실행 로그

명령:

```bash
npm run problems:external-audit
```

결과:

- 외부 풀이 후보: 29개
- Python/C++ 런타임으로 바로 검증 가능한 후보: 17개
- Java 런타임 추가 또는 Python/C++ 포팅이 필요한 후보: 12개
- 언어 분포:
  - Python: 10개
  - C++: 9개
  - Java: 16개

출력:

- `data/external-solution-audit.json`
- `docs/external-solution-audit.md`

명령:

```bash
npm run problems:batch-01
```

결과:

- 1차 편입 후보 17개를 별도 batch로 묶었다.
- 이 batch는 아직 서비스 편입 완료가 아니다.
- 문제 요약, sample, edge/fuzz, oracle 검증 후 실제 `data/problems.json`에 넣는다.

출력:

- `data/problem-expansion-batch-01.json`
- `docs/phases/phase-13-batch-01-external-runtime.md`

명령:

```bash
node scripts/fetch-boj-statements.mjs --only=4949,11256,11441,11663,11728 --delay=500
node scripts/fetch-boj-statements.mjs --only=1238,1497,1697,2156,2602,2638,3025,4949,11256,11441,11663,11728,14284,14697,15886,17142,21944 --delay=500
```

결과:

- statement/sample 확보 성공:
  - 1238 파티
  - 1697 숨바꼭질
  - 2156 포도주 시식
  - 2602 돌다리 건너기
  - 2638 치즈
  - 4949 균형잡힌 세상
  - 11256 사탕
  - 11441 합 구하기
- statement 확보 실패 또는 재시도 필요:
  - 1497, 3025, 11663, 11728, 14284, 14697, 15886, 17142, 21944
- `fetch-boj-statements.mjs`가 성공 캐시를 뒤이은 실패로 덮어쓰지 않도록 수정했다.

명령:

```bash
npm run problems:first-5
```

결과:

- 첫 편입 검토 후보 5개를 분리했다.
- 후보:
  - 4949 균형잡힌 세상
  - 11256 사탕
  - 11441 합 구하기
  - 1697 숨바꼭질
  - 2156 포도주 시식

출력:

- `data/problem-expansion-first-5.json`
- `docs/phases/phase-13-first-5.md`

명령:

```bash
npm run problems:import-first-5
npm run data:map
npx next build
```

결과:

- 첫 5문제를 `data/problems-extra.json`으로 편입했다.
- `data/problems.json`은 생성 파일로 유지하고, 확장 문제는 별도 파일에서 관리한다.
- 앱 데이터 로더와 포켓몬 매핑 스크립트가 기본 문제 + 확장 문제를 함께 보도록 변경했다.
- `monster-map` 매핑 수: 367개
- Next.js build 통과

편입 후 재감사:

- 현재 앱 문제 수: 358개 unique BOJ 문제
- 추가 필요 문제 수: 667개
- 현재 앱에 없는 후보: 637개
- 외부 풀이 후보: 24개
- Python/C++ 런타임 후보 batch: 12개

첫 5문제 override 보강:

- `data_structure-4949`
- `greedy-11256`
- `prefix_sum-11441`
- `graph_traversal-1697`
- `dynamic_programming_1-2156`

검증:

- 첫 5문제 override self-judge 모두 AC
- `npm run judge:coverage`: 367개 전부 judge ready
- `npm run judge:audit`: missing case 0개
- `npm run judge:lang-audit`: 확장 문제 포함 통과
- `npx next build`: 통과

### Batch 02. 100개 후보 확대

명령:

```bash
npm run problems:batch-02
```

결과:

- 100개 후보를 크게 잡았다.
- lane 분포:
  - `external_runtime`: 12개
  - `external_java_or_port`: 12개
  - `manual_oracle`: 76개
- 초기 준비 상태:
  - `ready_for_override`: 3개
  - `needs_statement`: 9개
  - `needs_statement_and_oracle`: 88개

statement 보강 명령:

```bash
node scripts/fetch-boj-statements.mjs --only=15886,14697,21944,11663,11728,2638,17142,1497,1238,14284,2602,3025,12931,18234,1034,7453,13422,2293,12026,18232,1507,17396,20007,2637,1159,1213,1259,1622,1718,1942 --delay=500
```

결과:

- 시간 제한으로 전체 완료 전 중단됐지만, 중간 저장으로 일부 확보했다.
- 새로 statement 확보:
  - 15886 내 선물을 받아줘 2
  - 14697 방 배정하기
- 기존 확보 포함 현재 `ready_for_override`: 5개
- 재실행 후 상태:
  - `ready_for_override`: 5개
  - `needs_statement`: 7개
  - `needs_statement_and_oracle`: 88개

출력:

- `data/problem-expansion-batch-02.json`
- `docs/phases/phase-13-batch-02-100-candidates.md`

### Batch 02. 두 번째 5문제 편입

편입 대상:

- `implementation-15886` 내 선물을 받아줘 2
- `brute_force-14697` 방 배정하기
- `graph_traversal-2638` 치즈
- `shortest_path-1238` 파티
- `dynamic_programming_2-2602` 돌다리 건너기

명령:

```bash
npm run problems:import-batch-02-ready
python scripts/verify-judge-overrides.py implementation-15886 brute_force-14697 graph_traversal-2638 shortest_path-1238 dynamic_programming_2-2602
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

결과:

- `data/problems-extra.json` 확장 문제 수: 10개
- 전체 포켓몬 매핑 수: 372개
- 두 번째 5문제 override self-judge: 모두 AC
- judge coverage: 372개 전부 judge ready
- missing case: 0개
- Next.js build 통과

편입 후 재감사:

- 현재 앱 문제 수: 363개 unique BOJ 문제
- 추가 필요 문제 수: 662개
- 현재 앱에 없는 후보: 632개
- 외부 풀이 후보: 19개
- 다음 Batch 02 상태:
  - `external_runtime`: 7개
  - `external_java_or_port`: 12개
  - `manual_oracle`: 81개
  - `ready_for_override`: 0개

### Batch 02. 네 번째 5문제 수동 string 배치

추가로 문자열 규칙형 문제 5개를 편입했다. 이번 묶음은 정렬, 치환, ROT13, 접미사 정렬, 공백 포함 암호 규칙을 포함한다.

입력한 문제:

- `string-1213` 팰린드롬 만들기
- `string-1718` 암호
- `string-2941` 크로아티아 알파벳
- `string-11655` ROT13
- `string-11656` 접미사 배열

추가 파일:

- `harness/overrides/string-1213.py`
- `harness/overrides/string-1718.py`
- `harness/overrides/string-2941.py`
- `harness/overrides/string-11655.py`
- `harness/overrides/string-11656.py`

검증 명령:

```bash
npm run problems:import-manual-strings
python scripts/verify-judge-overrides.py string-1213 string-1718 string-2941 string-11655 string-11656
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 새 5문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 382개
- judge coverage: 382개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

주의:

- `npm run problems:expansion-audit`는 GitHub API rate limit 403으로 실패했다.
- 따라서 후보 재계산 문서는 rate limit 해제 후 다시 생성해야 한다.
- 현재 확정된 앱 문제 수는 기존 unique 353개 + 확장 unique 20개 = 373개다.
- 목표 1025개까지 남은 unique 문제 수는 652개다.

### Batch 02. 다섯 번째 5문제 수동 string 배치

추가로 문자열 문제 5개를 더 편입했다. 이번 묶음은 부분 문자열, 단어 치환, 팰린드롬 변형, 비밀번호 역순 탐색을 포함한다.

입력한 문제:

- `string-9933` 민균이의 비밀번호
- `string-11478` 서로 다른 부분 문자열의 개수
- `string-14405` 피카츄
- `string-15927` 회문은 회문아니야!!
- `string-16916` 부분 문자열

추가 파일:

- `harness/overrides/string-9933.py`
- `harness/overrides/string-11478.py`
- `harness/overrides/string-14405.py`
- `harness/overrides/string-15927.py`
- `harness/overrides/string-16916.py`

검증 명령:

```bash
npm run problems:import-manual-strings
python scripts/verify-judge-overrides.py string-9933 string-11478 string-14405 string-15927 string-16916
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 새 5문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 387개
- judge coverage: 387개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 기존 unique BOJ 문제: 353개
- 확장 unique BOJ 문제: 25개
- 총 unique BOJ 문제: 378개
- 목표 1025개까지 남은 unique 문제 수: 647개

### Batch 02. 여섯 번째 5문제 수동 string 배치

문자열 후보 중 규칙 검증이 비교적 명확한 문제 5개를 추가 편입했다. 이번 묶음은 공통 문자, 놀라운 문자열, 정규식 판정, 경기 리드 시간 계산, Java/C++ 변수명 변환을 포함한다.

입력한 문제:

- `string-1622` 공통 순열
- `string-1972` 놀라운 문자열
- `string-2671` 잠수함식별
- `string-2852` NBA 농구
- `string-3613` Java vs C++

추가 파일:

- `harness/overrides/string-1622.py`
- `harness/overrides/string-1972.py`
- `harness/overrides/string-2671.py`
- `harness/overrides/string-2852.py`
- `harness/overrides/string-3613.py`

검증 명령:

```bash
npm run problems:import-manual-strings
python scripts/verify-judge-overrides.py string-1622 string-1972 string-2671 string-2852 string-3613
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 새 5문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 392개
- judge coverage: 392개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 기존 unique BOJ 문제: 353개
- 확장 unique BOJ 문제: 30개
- 총 unique BOJ 문제: 383개
- 목표 1025개까지 남은 unique 문제 수: 642개

### Batch 02. 일곱 번째 5문제 수동 string 배치

문자열 후보 5개를 추가 편입하면서, `harness/judge_core.py`의 override 입력 처리 버그도 함께 수정했다. 기존 override는 `edge`, `stress`, `fuzz` helper가 만든 dict 형태의 케이스를 반환할 수 있는데, judge가 이를 문자열 stdin으로만 취급하던 문제가 있었다. 이제 dict 케이스의 `input`, `kind`, `expected`를 정식으로 해석한다.

입력한 문제:

- `string-5534` 간판
- `string-6996` 애너그램
- `string-9536` 여우는 어떻게 울지?
- `string-13022` 늑대와 올바른 단어
- `string-20944` 팰린드롬 척화비

추가 파일:

- `harness/overrides/string-5534.py`
- `harness/overrides/string-6996.py`
- `harness/overrides/string-9536.py`
- `harness/overrides/string-13022.py`
- `harness/overrides/string-20944.py`

수정 파일:

- `harness/judge_core.py`

검증 명령:

```bash
npm run problems:import-manual-strings
python scripts/verify-judge-overrides.py string-5534 string-6996 string-9536 string-13022 string-20944
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 새 5문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 397개
- judge coverage: 397개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 기존 unique BOJ 문제: 353개
- 확장 unique BOJ 문제: 35개
- 총 unique BOJ 문제: 388개
- 목표 1025개까지 남은 unique 문제 수: 637개

### Batch 02. 여덟 번째 5문제 수동 math 배치

문자열 묶음 이후, 수학 후보 중 규칙이 명확하고 oracle을 짧게 검증할 수 있는 5개를 추가 편입했다.

입력한 문제:

- `math-1188` 음식 평론가
- `math-1456` 거의 소수
- `math-1669` 멍멍이 쓰다듬기
- `math-2168` 타일 위의 대각선
- `math-2436` 공약수

추가 파일:

- `harness/overrides/math-1188.py`
- `harness/overrides/math-1456.py`
- `harness/overrides/math-1669.py`
- `harness/overrides/math-2168.py`
- `harness/overrides/math-2436.py`

검증 명령:

```bash
npm run problems:import-manual-strings
python scripts/verify-judge-overrides.py math-1188 math-1456 math-1669 math-2168 math-2436
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 새 5문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 402개
- judge coverage: 402개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 기존 unique BOJ 문제: 353개
- 확장 unique BOJ 문제: 40개
- 총 unique BOJ 문제: 393개
- 목표 1025개까지 남은 unique 문제 수: 632개

### Batch 02. 아홉 번째 10문제 수동 mixed 배치

요청에 따라 배치 크기를 10개로 키웠다. 이번 묶음은 수학 2개, 구현 5개, 누적합 3개로 구성했다.

입력한 문제:

- `math-2553` 마지막 팩토리얼 수
- `math-2824` 최대공약수
- `implementation-2877` 4와 7
- `implementation-5766` 할아버지는 유명해!
- `implementation-9081` 단어 맞추기
- `implementation-9934` 완전 이진 트리
- `implementation-10703` 유성
- `prefix_sum-16139` 인간-컴퓨터 상호작용
- `prefix_sum-16507` 어두운 건 무서워
- `prefix_sum-19951` 태상이의 훈련소 생활

추가 파일:

- `harness/overrides/math-2553.py`
- `harness/overrides/math-2824.py`
- `harness/overrides/implementation-2877.py`
- `harness/overrides/implementation-5766.py`
- `harness/overrides/implementation-9081.py`
- `harness/overrides/implementation-9934.py`
- `harness/overrides/implementation-10703.py`
- `harness/overrides/prefix_sum-16139.py`
- `harness/overrides/prefix_sum-16507.py`
- `harness/overrides/prefix_sum-19951.py`

검증 명령:

```bash
npm run problems:import-manual-strings
python scripts/verify-judge-overrides.py math-2553 math-2824 implementation-2877 implementation-5766 implementation-9081 implementation-9934 implementation-10703 prefix_sum-16139 prefix_sum-16507 prefix_sum-19951
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 새 10문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 412개
- judge coverage: 412개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 기존 unique BOJ 문제: 353개
- 확장 unique BOJ 문제: 50개
- 총 unique BOJ 문제: 403개
- 목표 1025개까지 남은 unique 문제 수: 622개

### Batch 02. 열 번째 20문제 수동 mixed 배치

요청에 따라 배치 크기를 20개로 키웠다. 이번 묶음은 이분 탐색, 투 포인터, DP, 최단 경로, 위상 정렬, 그리디, 누적합, 구현을 섞었다.

입력한 문제:

- `binary_search-11663` 선분 위의 점
- `two_pointer-11728` 배열 합치기
- `dynamic_programming_1-2293` 동전 1
- `dynamic_programming_1-12026` BOJ 거리
- `two_pointer-13422` 도둑
- `shortest_path-14284` 간선 이어가기 2
- `topological_sorting-2637` 장난감 조립
- `binary_search-7453` 합이 0인 네 정수
- `shortest_path-1507` 궁금한 민호
- `greedy-12931` 두 배 더하기
- `greedy-18234` 당근 훔쳐 먹기
- `prefix_sum-2571` 색종이 - 3
- `prefix_sum-3673` 나눌 수 있는 부분 수열
- `prefix_sum-5549` 행성 탐사
- `prefix_sum-10713` 기차 여행
- `prefix_sum-14476` 최대공약수 하나 빼기
- `prefix_sum-17390` 이건 꼭 풀어야 해!
- `prefix_sum-17123` 배열 놀이
- `dynamic_programming_2-20002` 사과나무
- `implementation-17128` 소가 정보섬에 올라온 이유

추가 파일:

- `scripts/import-expansion-manual-batch-04.mjs`
- `harness/overrides/binary_search-11663.py`
- `harness/overrides/two_pointer-11728.py`
- `harness/overrides/dynamic_programming_1-2293.py`
- `harness/overrides/dynamic_programming_1-12026.py`
- `harness/overrides/two_pointer-13422.py`
- `harness/overrides/shortest_path-14284.py`
- `harness/overrides/topological_sorting-2637.py`
- `harness/overrides/binary_search-7453.py`
- `harness/overrides/shortest_path-1507.py`
- `harness/overrides/greedy-12931.py`
- `harness/overrides/greedy-18234.py`
- `harness/overrides/prefix_sum-2571.py`
- `harness/overrides/prefix_sum-3673.py`
- `harness/overrides/prefix_sum-5549.py`
- `harness/overrides/prefix_sum-10713.py`
- `harness/overrides/prefix_sum-14476.py`
- `harness/overrides/prefix_sum-17390.py`
- `harness/overrides/prefix_sum-17123.py`
- `harness/overrides/dynamic_programming_2-20002.py`
- `harness/overrides/implementation-17128.py`

함께 수정한 내용:

- `data/categories.json`에 `topological_sorting` 카테고리를 추가했다.
- 빌드 중 `/problem/topological_sorting-2637`에서 카테고리 메타가 없어 `slug` 접근 에러가 난 문제를 해결했다.

검증 명령:

```bash
node scripts/import-expansion-manual-batch-04.mjs
python scripts/verify-judge-overrides.py binary_search-11663 two_pointer-11728 dynamic_programming_1-2293 dynamic_programming_1-12026 two_pointer-13422 shortest_path-14284 topological_sorting-2637 binary_search-7453 shortest_path-1507 greedy-12931 greedy-18234 prefix_sum-2571 prefix_sum-3673 prefix_sum-5549 prefix_sum-10713 prefix_sum-14476 prefix_sum-17390 prefix_sum-17123 dynamic_programming_2-20002 implementation-17128
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 새 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 432개
- judge coverage: 432개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 기존 unique BOJ 문제: 353개
- 확장 unique BOJ 문제: 70개
- 총 unique BOJ 문제: 423개
- 목표 1025개까지 남은 unique 문제 수: 602개

### Batch 02. 세 번째 5문제 수동 string 배치

외부 정답 후보 중 남은 7개 `external_runtime` 문제는 현재 statement 수집이 막혀 있어, 바로 검증 가능한 수동 oracle 문제부터 진행했다.

입력한 문제:

- `string-1159` 농구 경기
- `string-1259` 팰린드롬수
- `string-10808` 알파벳 개수
- `string-10809` 알파벳 찾기
- `string-10988` 팰린드롬인지 확인하기

추가 파일:

- `scripts/import-expansion-manual-strings.mjs`
- `harness/overrides/string-1159.py`
- `harness/overrides/string-1259.py`
- `harness/overrides/string-10808.py`
- `harness/overrides/string-10809.py`
- `harness/overrides/string-10988.py`

검증 명령:

```bash
npm run problems:import-manual-strings
python scripts/verify-judge-overrides.py string-1159 string-1259 string-10808 string-10809 string-10988
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 새 5문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 377개
- judge coverage: 377개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

재감사 결과:

- 현재 앱 문제 수: 368개 unique BOJ 문제
- 추가 필요 문제 수: 657개
- 현재 앱에 없는 후보: 627개
- 외부 풀이 후보: 19개
- 다음 Batch 02 상태:
  - `external_runtime`: 7개
  - `external_java_or_port`: 12개
  - `manual_oracle`: 81개
  - `ready_for_override`: 0개

### 열한 번째 10문제 수동 mixed 배치

20개 단위 확장을 이어가되, 남은 후보 중 규칙이 명확한 문제를 우선 선별해 10문제를 먼저 편입했다. 이번 배치는 문자열 파싱, 수학 최적화, 구현, 브루트포스, BFS 문제로 구성했다.

편입 문제:

- `string-1942`, `string-3005`, `string-3107`, `string-20114`
- `math-3343`, `math-9421`
- `implementation-1022`, `implementation-1283`
- `brute_force-1034`
- `graph_traversal-18232`

검증 명령:

```bash
node scripts/import-expansion-manual-batch-05.mjs
python scripts/verify-judge-overrides.py string-1942 string-3005 string-3107 string-20114 math-3343 math-9421 implementation-1022 implementation-1283 brute_force-1034 graph_traversal-18232
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 신규 10문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 442개
- judge coverage: 442개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 확장 unique BOJ 문제: 80개
- 총 unique BOJ 문제: 433개
- 목표 1025개까지 남은 unique 문제 수: 592개

### 열두 번째 10문제 수동 mixed 배치

직전 10문제에 이어 다음 10문제를 추가했다. 이로써 이번 요청의 20문제 단위 확장은 452개 judge-ready 상태까지 완료되었다.

편입 문제:

- `backtracking-1497`
- `shortest_path-17396`, `shortest_path-20007`
- `data_structure2-19583`
- `implementation-16719`, `implementation-16927`, `implementation-17276`, `implementation-18311`, `implementation-20164`, `implementation-2469`

검증 명령:

```bash
node scripts/import-expansion-manual-batch-06.mjs
python scripts/verify-judge-overrides.py backtracking-1497 shortest_path-17396 shortest_path-20007 data_structure2-19583 implementation-16719 implementation-16927 implementation-17276 implementation-18311 implementation-20164 implementation-2469
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 신규 10문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 452개
- judge coverage: 452개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 확장 unique BOJ 문제: 90개
- 총 unique BOJ 문제: 443개
- 목표 1025개까지 남은 unique 문제 수: 582개

### 열세 번째 고난도 6문제 수동 mixed 배치

남은 후보 중 원문 규칙을 안정적으로 재현할 수 있는 고난도 문제 6개를 추가했다. 배열 회전 계열과 추천 시스템, 연구소 3처럼 학생 제출에서 오류가 자주 날 수 있는 문제를 우선했다.

편입 문제:

- `graph_traversal-17142`
- `implementation-17406`, `implementation-17470`, `implementation-20327`, `implementation-21277`
- `data_structure2-21944`

검증 명령:

```bash
node scripts/import-expansion-manual-batch-07.mjs
python scripts/verify-judge-overrides.py graph_traversal-17142 implementation-17406 implementation-17470 implementation-20327 implementation-21277 data_structure2-21944
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 신규 6문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 458개
- judge coverage: 458개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 확장 unique BOJ 문제: 96개
- 총 unique BOJ 문제: 449개
- 목표 1025개까지 남은 unique 문제 수: 576개

### 열네 번째 문자열/수학/구현 7문제 수동 배치

남은 후보 중 문자열 특수 규칙과 수학 조건을 확인할 수 있는 7문제를 추가했다. 특히 `string-20210`은 자연 정렬 규칙, `math-22943`은 소수 합/곱 조건을 override에 포함했다.

편입 문제:

- `string-4446`, `string-9242`, `string-19844`, `string-19948`, `string-20210`
- `implementation-22858`
- `math-22943`

검증 명령:

```bash
node scripts/import-expansion-manual-batch-08.mjs
python scripts/verify-judge-overrides.py string-4446 string-9242 string-19844 string-19948 string-20210 implementation-22858 math-22943
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 신규 7문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 465개
- judge coverage: 465개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 확장 unique BOJ 문제: 103개
- 총 unique BOJ 문제: 456개
- 목표 1025개까지 남은 unique 문제 수: 569개

### 열다섯 번째 prefix/구현 5문제 수동 배치

GitHub Action의 Docker runner 인자 호환 문제를 커밋/푸시한 뒤, 남은 후보 중 규칙을 안정적으로 재현할 수 있는 5문제를 추가했다.

편입 문제:

- `prefix_sum-10427`, `prefix_sum-18866`, `prefix_sum-19566`
- `implementation-22859`, `implementation-22860`

검증 명령:

```bash
node scripts/import-expansion-manual-batch-09.mjs
python scripts/verify-judge-overrides.py prefix_sum-10427 prefix_sum-18866 prefix_sum-19566 implementation-22859 implementation-22860
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 신규 5문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 470개
- judge coverage: 470개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 확장 unique BOJ 문제: 108개
- 총 unique BOJ 문제: 461개
- 목표 1025개까지 남은 unique 문제 수: 564개

### 열여섯 번째 batch-02 마감 partial 7문제 배치

사용자 요청에 따라 이후 배치는 20개 단위로 처리하고, 각 배치 종료 시 남은 문제 수를 기록하며, 배치마다 commit/push 한다. 다만 현재 batch-02 후보는 7개만 남아 있었기 때문에 마지막 partial batch로 마감했다.

편입 문제:

- `simulation-3025`
- `string-2115`, `string-4836`, `string-16890`
- `implementation-21611`
- `prefix_sum-2900`, `prefix_sum-5875`

검증 명령:

```bash
node scripts/import-expansion-manual-batch-10.mjs
python scripts/verify-judge-overrides.py simulation-3025 string-2115 string-4836 string-16890 implementation-21611 prefix_sum-2900 prefix_sum-5875
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 신규 7문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 477개
- judge coverage: 477개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- batch-02 남은 후보: 0개
- 확장 unique BOJ 문제: 115개
- 총 unique BOJ 문제: 468개
- 목표 1025개까지 남은 unique 문제 수: 557개
### Batch 03: 그리디 20문제 확장

사용자 요청에 따라 앞으로의 문제 확장은 20개 단위로 처리하고, 각 배치가 끝날 때마다 남은 개수를 기록한 뒤 commit/push한다. 이번 배치는 그리디 후보 중 oracle과 fuzz/edge 입력을 안정적으로 구성할 수 있는 20문제를 추가했다.

도입 문제:

- `greedy-1080`, `greedy-1343`, `greedy-1439`, `greedy-1449`, `greedy-1455`
- `greedy-1715`, `greedy-1744`, `greedy-1946`, `greedy-2138`, `greedy-2847`
- `greedy-6068`, `greedy-11047`, `greedy-11509`, `greedy-12782`, `greedy-13413`
- `greedy-14400`, `greedy-16162`, `greedy-16206`, `greedy-17615`, `greedy-19939`

검증 명령:

```bash
node scripts/import-expansion-manual-batch-11.mjs
python scripts/verify-judge-overrides.py greedy-1080 greedy-1343 greedy-1439 greedy-1449 greedy-1455 greedy-1715 greedy-1744 greedy-1946 greedy-2138 greedy-2847 greedy-6068 greedy-11047 greedy-11509 greedy-12782 greedy-13413 greedy-14400 greedy-16162 greedy-16206 greedy-17615 greedy-19939
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 497개
- judge coverage: 497개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 이번 배치 처리: 20개
- 확장 후보 기준 남은 문제: 507개

### Batch 04: 기본 구현/브루트포스/DP 20문제 확장

이번 배치는 정수/문자열 출력으로 정확 비교가 가능한 20문제를 추가했다. 부동소수 허용 오차가 필요한 문제는 special judge 정책을 먼저 잡은 뒤 별도 배치로 다룬다.

도입 문제:

- `dynamic_programming_1-1003`, `brute_force-1018`, `brute_force-1059`, `brute_force-1065`, `binary_search-1072`
- `brute_force-1120`, `dynamic_programming_1-1149`, `brute_force-1251`, `brute_force-1254`, `graph_traversal-1303`
- `dynamic_programming_1-1309`, `greedy-1374`, `brute_force-1411`, `brute_force-1421`, `greedy-1474`
- `two_pointer-1484`, `brute_force-1487`, `brute_force-1503`, `brute_force-1527`, `brute_force-1543`

검증 명령:

```bash
node scripts/import-expansion-manual-batch-12.mjs
python scripts/verify-judge-overrides.py dynamic_programming_1-1003 brute_force-1018 brute_force-1059 brute_force-1065 binary_search-1072 brute_force-1120 dynamic_programming_1-1149 brute_force-1251 brute_force-1254 graph_traversal-1303 dynamic_programming_1-1309 greedy-1374 brute_force-1411 brute_force-1421 greedy-1474 two_pointer-1484 brute_force-1487 brute_force-1503 brute_force-1527 brute_force-1543
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 517개
- judge coverage: 517개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

현재 확정 상태:

- 이번 배치 처리: 20개
- 확장 후보 기준 남은 문제: 487개
