# Judge Case Audit

## 현재 정책

- 기본 채점은 BOJ 예제 케이스를 먼저 사용한다.
- 예제가 없는 문제는 `harness/overrides/<problem-slug>.py`의 problem-specific case를 사용한다.
- category 공통 fuzz는 기본 비활성화 상태다.
- 잘못된 공통 fuzz가 문제 입력 형식을 깨면 정답 코드가 `oracle failed`로 실패할 수 있으므로, 문제별 입력 형식이 보장된 override를 우선한다.

## Audit 결과

2026-05-05 기준:

```txt
total: 362
judgeReady: 362
missingCases: 0
```

2026-05-06 Phase 08 1차 batch 이후:

```txt
overrides: 45
sampleOnly: 317
highRiskSampleOnly: 178
```

2026-05-06 Phase 08 2차 batch 이후:

```txt
overrides: 50
sampleOnly: 312
highRiskSampleOnly: 173
```

2026-05-06 Phase 08 3차 batch 이후:

```txt
overrides: 70
sampleOnly: 292
highRiskSampleOnly: 153
```

2026-05-06 `shortest_path-1719` oracle 수정 이후:

```txt
overrides: 71
sampleOnly: 291
highRiskSampleOnly: 152
```

2026-05-07 Phase 08 4차 batch 이후:

```txt
overrides: 91
sampleOnly: 271
highRiskSampleOnly: 132
```

2026-05-07 Phase 08 5차 batch 이후:

```txt
overrides: 111
sampleOnly: 251
highRiskSampleOnly: 112
```

2026-05-07 Phase 08 6차 batch 이후:

```txt
overrides: 131
sampleOnly: 231
highRiskSampleOnly: 92
```

2026-05-07 Phase 08 7차 batch 이후:

```txt
overrides: 151
sampleOnly: 211
highRiskSampleOnly: 72
```

2026-05-08 Phase 08 8차 batch 이후:

```txt
overrides: 171
sampleOnly: 191
highRiskSampleOnly: 52
```

2026-05-08 Phase 08 9차 batch 이후:

```txt
overrides: 191
sampleOnly: 171
highRiskSampleOnly: 32
```

즉, 현재 등록된 362개 문제는 모두 최소한 다음 중 하나를 가진다.

- BOJ 예제 케이스
- 문제별 deterministic override case

## 추가된 Override 범위

기존 override:

```txt
brute_force-2798
implementation-5597
```

Phase 07에서 추가한 missing-case override:

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

## 검증 결과

```txt
npm run judge:audit
-> total 362, judgeReady 362, missingCases 0

npm run harness:test
-> OK, 9 tests

npm run judge:verify-overrides
-> OK: 35 override files self-judged successfully.
```

추가로 33개 missing-case override 전체에 대해 정답 코드를 사용자 코드처럼 실행하는 self-judge를 수행했다.

```txt
33개 override 대상 문제
-> 모두 AC, 각 문제 6/6 cases 통과
```

Java 정답 코드에 한글 주석이 있는 문제(`graph_traversal-14940`)에서 Docker 내부 `javac`가 기본 인코딩을 US-ASCII로 잡아 CE가 발생했기 때문에, `javac -encoding UTF-8`로 고정했다.

Phase 08 4차 batch에서는 `minimum_spanning_tree-1647`의 Python oracle이 실제 BOJ 1647 입력 형식과 맞지 않는 것을 발견했다.

```txt
minimum_spanning_tree-1647
-> Python oracle을 Kruskal 기반 도시 분할 계획 풀이로 교체
-> N=2 경계 케이스 포함
-> self-judge AC
```

4차 batch 검증:

```txt
npm run judge:verify-overrides -- minimum_spanning_tree-1197 minimum_spanning_tree-1368 minimum_spanning_tree-1647 minimum_spanning_tree-1774 minimum_spanning_tree-1922 minimum_spanning_tree-2887 minimum_spanning_tree-4386 minimum_spanning_tree-6497 graph_traversal-1012 graph_traversal-2206 graph_traversal-11724 graph_traversal-11725 graph_traversal-17836 two_pointer-1940 two_pointer-2018 two_pointer-2230 two_pointer-2470 binary_search-1654 binary_search-1789 binary_search-1920
-> OK: 20 override files self-judged successfully.

npm run harness:test
-> OK, 9 tests
```

5차 batch 검증:

```txt
npm run judge:verify-overrides -- binary_search-2110 binary_search-2143 binary_search-2417 binary_search-2470 binary_search-2776 binary_search-6236 binary_search-9024 binary_search-10815 binary_search-10816 dynamic_programming_2-1005 dynamic_programming_1-1463 dynamic_programming_on_trees-2533 dynamic_programming_2-5557 dynamic_programming_1-11660 dynamic_programming_1-11726 dynamic_programming_1-13699 dynamic_programming_2-14567 dynamic_programming_1-14722 dynamic_programming_1-22869 backtracking-1182
-> OK: 20 override files self-judged successfully.

npm run harness:test
-> OK, 9 tests
```

6차 batch 검증 요약:

```txt
추가 override:
backtracking-1189, backtracking-2026, backtracking-2580, backtracking-9663, backtracking-10974,
simulation-5373,
prefix_sum-1749, prefix_sum-2167, prefix_sum-10986, prefix_sum-11659, prefix_sum-20440,
minimum_spanning_tree-16398, minimum_spanning_tree-20010,
graph_traversal-1260, graph_traversal-14502, graph_traversal-16918, graph_traversal-16953,
data_structure-1158, data_structure2-1269, data_structure2-1620

검증:
-> 20개 모두 self-judge AC 확인

npm run harness:test
-> OK, 9 tests
```

7차 batch 검증 요약:

```txt
추가 override:
data_structure2-1927, data_structure-1966, data_structure2-2075, data_structure-2164, data_structure-2346,
data_structure-2493, data_structure2-4358, data_structure-5397, data_structure-5430, data_structure2-7662,
data_structure-10845, data_structure2-11279, data_structure2-11286, data_structure2-14425, data_structure2-21939,
two_pointer-15961, two_pointer-20922,
binary_search-2512, binary_search-2805, binary_search-3079

수정한 oracle:
data_structure2-11279, data_structure-2346

검증:
-> 20개 모두 self-judge AC 확인

npm run harness:test
-> OK, 9 tests
```

8차 batch 검증 요약:

```txt
추가 override:
binary_search-19637, binary_search-20444,
dynamic_programming_1-1912, dynamic_programming_1-10164, dynamic_programming_1-11048, dynamic_programming_1-11727,
simulation-14503,
prefix_sum-2015, prefix_sum-11660, prefix_sum-20438, prefix_sum-21318,
minimum_spanning_tree-21924,
graph_traversal-2178, graph_traversal-13023, graph_traversal-20924, graph_traversal-1058, graph_traversal-7576, graph_traversal-16234, graph_traversal-16954,
data_structure-1874

수정한 oracle:
graph_traversal-20924, prefix_sum-20438

검증:
-> 20개 모두 self-judge AC 확인

npm run harness:test
-> OK, 9 tests
```

9차 batch 검증 요약:

```txt
추가 override:
data_structure-1935, data_structure-2504, data_structure-9012, data_structure-10799, data_structure-10828, data_structure-10866, data_structure-18115, data_structure-22942,
binary_search-1477,
dynamic_programming_1-1106, dynamic_programming_on_trees-1135, dynamic_programming_2-11985, dynamic_programming_1-15486, dynamic_programming_1-17626, dynamic_programming_1-2839, dynamic_programming_2-21923,
backtracking-1038, backtracking-14712, backtracking-14889, backtracking-15649

검증:
-> 20개 모두 self-judge AC 확인

npm run harness:test
-> OK, 9 tests
```

## 남은 작업

- `missingCases`는 0이 되었지만, 모든 BOJ hidden case를 완전히 복제한 것은 아니다.
- 다음 단계에서는 예제가 있는 문제 중에서도 오답이 쉽게 통과할 수 있는 문제부터 edge/stress override를 추가한다.
- 우선순위는 그래프, DP, 이분 탐색, 투 포인터, 백트래킹, 시뮬레이션처럼 예제만으로는 취약한 유형이다.
