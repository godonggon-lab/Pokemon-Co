# Phase 07. Judge Edge/Stress 강화

## 목표

예제 케이스만으로는 잡기 어려운 edge case, stress case, TLE/MLE 위험을 문제별로 보강한다.

이 단계의 1차 목표는 `docs/judge-case-audit.md`에서 확인된 `missingCases` 33개를 0으로 만드는 것이다.

## 배경

Phase 06에서 category 공통 fuzz를 기본 비활성화했다.

이유는 `implementation-5597`처럼 문제 입력 형식이 고정되어 있는 경우, 공통 fuzz가 `43 26` 같은 잘못된 입력을 만들어 정답 코드 자체가 실패할 수 있었기 때문이다. 채점기는 틀린 입력을 많이 만드는 것보다, 적은 수라도 형식이 보장된 입력을 넣는 편이 더 안전하다.

## 범위

- `JudgeCase.kind`를 `sample`, `edge`, `stress`, `fuzz`로 구분한다.
- `AC`, `WA`, `TLE`, `MLE`, `RE`, `CE`, `OLE`, `PE` 판정을 명확히 한다.
- 출력 초과(`OLE`)와 출력 형식 오류(`PE`)를 분리한다.
- 문제별 override에서 `edge()`, `stress()`, `fuzz()` helper를 사용할 수 있게 한다.
- 예제나 override가 없는 33개 문제에 deterministic override를 추가한다.
- C++/Java 오라클만 있는 문제는 로컬 컴파일러 의존을 줄이기 위해 expected output을 함께 기록한다.

## 완료 기준

- `npm run judge:audit` 결과 `missingCases: 0`
- 33개 missing-case override가 모두 import 가능
- 33개 missing-case override를 정답 코드로 self-judge했을 때 모두 AC
- Java/C++ 실행 환경 문제로 채점 서버가 crash하지 않음

## 작업 로그

- `harness/judge_core.py`에 `OLE` 판정을 추가했다.
- `harness/judge_core.py`에 `PE` 판정을 추가했다. 토큰은 같지만 줄/공백 배치가 다르면 `PE`가 된다.
- runner 출력 제한을 `max_output_bytes`로 전달하도록 LocalRunner, DockerRunner, judge server를 확장했다.
- `harness/cases.py`를 추가해 override에서 `edge()`, `stress()`, `fuzz()` helper를 사용할 수 있게 했다.
- category 공통 fuzz는 `JUDGE_ENABLE_GENERIC_FUZZ=1`일 때만 켜지도록 유지했다.
- `implementation-5597` override를 추가해 28명 제출 입력 형식을 보장했다.
- Java 코드에 한글 주석이 있어도 Docker 안에서 컴파일되도록 `javac -encoding UTF-8`을 적용했다.
- 컴파일러나 런타임이 없을 때 LocalRunner가 서버를 crash시키지 않고 CE 형태로 반환하도록 보강했다.

## Missing Case 처리 결과

33개 missing-case override를 추가했다.

```txt
two_pointer-1806
dynamic_programming_1-1890
dynamic_programming_on_trees-1949
dynamic_programming_1-2294
brute_force-2309
two_pointer-2473
two_pointer-2559
graph_traversal-2589
graph_traversal-2606
data_structure2-2696
data_structure-2800
graph_traversal-5547
graph_traversal-7569
dynamic_programming_2-9251
dynamic_programming_1-9465
dynamic_programming_1-10870
greedy-11000
string-11720
dynamic_programming_2-11909
minimum_spanning_tree-14621
prefix_sum-14929
graph_traversal-14940
backtracking-15657
dynamic_programming_1-15989
graph_traversal-16174
dynamic_programming_on_trees-17831
data_structure-18258
backtracking-18430
greedy-19598
implementation-20053
greedy-20115
simulation-20165
prefix_sum-21757
```

## 실행 결과(Output)

Audit:

```txt
npm run judge:audit
-> total 362
-> judgeReady 362
-> missingCases 0
```

Unit test:

```txt
npm run harness:test
-> OK, 9 tests
```

Override self-judge:

```txt
npm run judge:verify-overrides
-> OK: 35 override files self-judged successfully.
```

Docker image rebuild:

```txt
docker build -t dongjun-coderunner:latest judge
-> build success
```

33개 missing-case override self-judge:

```txt
two_pointer-1806                         python  AC 6/6
dynamic_programming_1-1890               python  AC 6/6
dynamic_programming_on_trees-1949        cpp     AC 6/6
brute_force-2309                         python  AC 6/6
two_pointer-2473                         python  AC 6/6
graph_traversal-2589                     python  AC 6/6
graph_traversal-2606                     cpp     AC 6/6
data_structure2-2696                     cpp     AC 6/6
data_structure-2800                      python  AC 6/6
graph_traversal-5547                     cpp     AC 6/6
graph_traversal-7569                     python  AC 6/6
dynamic_programming_1-9465               python  AC 6/6
dynamic_programming_2-11909              python  AC 6/6
minimum_spanning_tree-14621              cpp     AC 6/6
graph_traversal-14940                    java    AC 6/6
backtracking-15657                       python  AC 6/6
dynamic_programming_1-15989              cpp     AC 6/6
graph_traversal-16174                    python  AC 6/6
dynamic_programming_on_trees-17831       python  AC 6/6
backtracking-18430                       cpp     AC 6/6
simulation-20165                         cpp     AC 6/6
prefix_sum-21757                         cpp     AC 6/6
string-11720                             python  AC 6/6
dynamic_programming_1-10870              cpp     AC 6/6
implementation-20053                     cpp     AC 6/6
greedy-20115                             python  AC 6/6
prefix_sum-14929                         cpp     AC 6/6
two_pointer-2559                         python  AC 6/6
dynamic_programming_2-9251               python  AC 6/6
dynamic_programming_1-2294               python  AC 6/6
greedy-11000                             python  AC 6/6
greedy-19598                             python  AC 6/6
data_structure-18258                     python  AC 6/6
```

## 남은 리스크

- `missingCases`는 0이지만, 이것이 BOJ hidden judge 전체를 복제했다는 뜻은 아니다.
- 현재는 "채점 불가 문제 제거"와 "명백한 입력 형식 오류 제거"가 핵심 성과다.
- 다음 작업은 예제가 있는 문제 중에서도 예제만 맞추는 코드가 통과하기 쉬운 문제를 골라 추가 override를 넣는 것이다.
- TLE/MLE는 문제별 최대 입력과 시간 제한이 필요하므로, stress case를 무조건 크게 만들기보다 문제별로 안전하게 늘려야 한다.
