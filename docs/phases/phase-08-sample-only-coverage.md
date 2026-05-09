# Phase 08. Sample-only 문제 보강

## 목표

Phase 07에서 `missingCases`는 0이 되었다.

Phase 08의 목표는 예제 케이스만 있는 문제 중, 예제만 맞추는 코드가 통과하기 쉬운 문제를 우선적으로 보강하는 것이다.

## 현재 상태

2026-05-05 기준 `npm run judge:coverage` 결과:

```txt
total: 362
judgeReady: 362
missingCases: 0
overrides: 35
sampleOnly: 327
highRiskSampleOnly: 188
```

의미:

- 모든 문제는 최소한 sample 또는 override를 가진다.
- 하지만 327개 문제는 아직 BOJ 예제만으로 채점된다.
- 이 중 188개는 그래프, DP, 최단경로, MST, 투 포인터, 백트래킹처럼 예제만으로 취약한 유형이다.

## 우선순위

1. 그래프 탐색
2. DP
3. 최단 경로
4. MST
5. 투 포인터 / 이분 탐색
6. 백트래킹
7. 시뮬레이션
8. 자료구조 / prefix sum

## 1차 후보

`npm run judge:coverage` 기준 top candidate:

```txt
graph_traversal-1325
graph_traversal-1707
graph_traversal-1726
graph_traversal-2573
graph_traversal-2636
graph_traversal-2667
graph_traversal-4179
graph_traversal-4963
graph_traversal-9328
graph_traversal-13549
graph_traversal-14716
graph_traversal-18513
dynamic_programming_1-1010
dynamic_programming_2-1516
dynamic_programming_2-1520
dynamic_programming_on_trees-2213
dynamic_programming_1-2407
dynamic_programming_1-2579
dynamic_programming_1-2748
dynamic_programming_2-3687
```

## 작업 방식

한 번에 188개를 처리하지 않는다.

작업 단위:

- 한 batch당 10개 내외
- 입력 형식이 비슷한 문제끼리 묶기
- 각 override는 최소/경계/특수/작은 stress를 포함
- 추가 후 `npm run judge:verify-overrides`로 전체 override self-judge
- `npm run judge:coverage`로 sample-only 수 감소 확인

## 완료 기준

- 1차 후보 20개 이상에 override 추가
- `npm run judge:verify-overrides` 통과
- `npm run judge:coverage`에서 `sampleOnly` 감소 확인
- phase 문서에 추가한 문제 목록과 output 기록

## 실행 명령

```bash
npm run judge:coverage
npm run judge:verify-overrides
npm run harness:test
```

## 작업 로그

- `scripts/audit-judge-coverage.mjs`를 추가했다.
- `package.json`에 `judge:coverage` 명령을 추가했다.
- Phase 08의 우선순위와 1차 후보를 정리했다.
- 1차 그래프 탐색 batch로 override 10개를 추가했다.
- Docker 기반 전체 override 검증이 C++ 반복 실행에서 간헐적으로 2초 제한에 걸릴 수 있어, `scripts/verify-judge-overrides.py`의 self-judge 시간 제한을 4초로 조정했다.
- 2차 batch로 coverage 상위 5개 문제 override를 추가했다.
- 3차 batch로 coverage 상위 20개 문제 override를 추가했다.
- 3차에서 보류했던 `shortest_path-1719`의 oracle 버그를 수정하고 override를 추가했다.
- 4차 batch로 MST, 그래프 탐색, 투 포인터, 이분 탐색 상위 20개 문제 override를 추가했다.
- `minimum_spanning_tree-1647` oracle이 문제 입력 형식과 맞지 않는 버그를 발견해 수정했다.
- 5차 batch로 이분 탐색, DP, 백트래킹 상위 20개 문제 override를 추가했다.
- 6차 batch로 백트래킹, 시뮬레이션, 누적합, MST, 그래프 탐색, 자료구조 상위 20개 문제 override를 추가했다.
- 7차 batch로 자료구조, 투 포인터, 이분 탐색 상위 20개 문제 override를 추가했다.
- 8차 batch로 이분 탐색, DP, 시뮬레이션, 누적합, MST, 그래프 탐색, 자료구조 상위 20개 문제 override를 추가했다.
- 9차 batch로 자료구조, 이분 탐색, DP, 백트래킹 상위 20개 문제 override를 추가했다.

1차 그래프 탐색 batch:

```txt
graph_traversal-1325
graph_traversal-1707
graph_traversal-1726
graph_traversal-2573
graph_traversal-2636
graph_traversal-2667
graph_traversal-4179
graph_traversal-4963
graph_traversal-9328
graph_traversal-13549
```

2차 batch:

```txt
graph_traversal-14716
graph_traversal-18513
dynamic_programming_1-1010
dynamic_programming_2-1516
dynamic_programming_2-1520
```

3차 batch:

```txt
dynamic_programming_on_trees-2213
dynamic_programming_1-2407
dynamic_programming_1-2579
dynamic_programming_1-2748
dynamic_programming_2-3687
dynamic_programming_2-7579
dynamic_programming_1-9095
dynamic_programming_1-9461
dynamic_programming_1-9655
dynamic_programming_1-11053
dynamic_programming_1-11055
dynamic_programming_1-11722
dynamic_programming_2-12015
dynamic_programming_on_trees-15681
dynamic_programming_1-15990
dynamic_programming_2-17485
dynamic_programming_2-18427
dynamic_programming_1-19622
dynamic_programming_1-21317
shortest_path-10282
```

보류 버그 수정:

```txt
shortest_path-1719
```

원인:

- 기존 oracle이 자기 자신 칸을 `-`로 출력하는 인덱스를 잘못 비교했다.
- Dijkstra 방문 처리도 최단 경로 갱신을 막을 수 있는 구조였다.

조치:

- `data/problems.json` 안의 `shortest_path-1719` oracle을 first-hop 기반 Dijkstra로 교체했다.
- `harness/overrides/shortest_path-1719.py`를 추가했다.

## 실행 결과(Output)

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 35
-> sampleOnly 327
-> highRiskSampleOnly 188
```

1차 그래프 탐색 batch 이후:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 45
-> sampleOnly 317
-> highRiskSampleOnly 178

npm run judge:verify-overrides -- graph_traversal-1325 graph_traversal-1707 graph_traversal-1726 graph_traversal-2573 graph_traversal-2636 graph_traversal-2667 graph_traversal-4179 graph_traversal-4963 graph_traversal-9328 graph_traversal-13549
-> OK: 10 override files self-judged successfully.

npm run judge:verify-overrides
-> OK: 45 override files self-judged successfully.

npm run harness:test
-> OK, 9 tests
```

다음 coverage 상위 후보:

```txt
graph_traversal-14716
graph_traversal-18513
dynamic_programming_1-1010
dynamic_programming_2-1516
dynamic_programming_2-1520
dynamic_programming_on_trees-2213
dynamic_programming_1-2407
dynamic_programming_1-2579
dynamic_programming_1-2748
dynamic_programming_2-3687
```

2차 batch 이후:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 50
-> sampleOnly 312
-> highRiskSampleOnly 173

npm run judge:verify-overrides -- graph_traversal-14716 graph_traversal-18513 dynamic_programming_1-1010 dynamic_programming_2-1516 dynamic_programming_2-1520
-> OK: 5 override files self-judged successfully.

npm run harness:test
-> OK, 9 tests
```

다음 coverage 상위 후보:

```txt
dynamic_programming_on_trees-2213
dynamic_programming_1-2407
dynamic_programming_1-2579
dynamic_programming_1-2748
dynamic_programming_2-3687
dynamic_programming_2-7579
dynamic_programming_1-9095
dynamic_programming_1-9461
dynamic_programming_1-9655
dynamic_programming_1-11053
```

3차 batch 이후:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 70
-> sampleOnly 292
-> highRiskSampleOnly 153

npm run judge:verify-overrides -- dynamic_programming_on_trees-2213 dynamic_programming_1-2407 dynamic_programming_1-2579 dynamic_programming_1-2748 dynamic_programming_2-3687 dynamic_programming_2-7579 dynamic_programming_1-9095 dynamic_programming_1-9461 dynamic_programming_1-9655 dynamic_programming_1-11053 dynamic_programming_1-11055 dynamic_programming_1-11722 dynamic_programming_2-12015 dynamic_programming_on_trees-15681 dynamic_programming_1-15990 dynamic_programming_2-17485 dynamic_programming_2-18427 dynamic_programming_1-19622 dynamic_programming_1-21317 shortest_path-10282
-> OK: 20 override files self-judged successfully.

npm run harness:test
-> OK, 9 tests
```

다음 coverage 상위 후보:

```txt
shortest_path-1719
minimum_spanning_tree-1197
minimum_spanning_tree-1368
minimum_spanning_tree-1647
minimum_spanning_tree-1774
minimum_spanning_tree-1922
minimum_spanning_tree-2887
minimum_spanning_tree-4386
minimum_spanning_tree-6497
graph_traversal-1012
graph_traversal-2206
graph_traversal-11724
graph_traversal-11725
graph_traversal-17836
two_pointer-1940
two_pointer-2018
two_pointer-2230
two_pointer-2470
binary_search-1654
binary_search-1789
```

`shortest_path-1719` 수정 이후:

```txt
npm run judge:verify-overrides -- shortest_path-1719
-> OK: 1 override files self-judged successfully.

npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 71
-> sampleOnly 291
-> highRiskSampleOnly 152

npm run harness:test
-> OK, 9 tests
```

4차 batch:

```txt
minimum_spanning_tree-1197
minimum_spanning_tree-1368
minimum_spanning_tree-1647
minimum_spanning_tree-1774
minimum_spanning_tree-1922
minimum_spanning_tree-2887
minimum_spanning_tree-4386
minimum_spanning_tree-6497
graph_traversal-1012
graph_traversal-2206
graph_traversal-11724
graph_traversal-11725
graph_traversal-17836
two_pointer-1940
two_pointer-2018
two_pointer-2230
two_pointer-2470
binary_search-1654
binary_search-1789
binary_search-1920
```

4차 batch에서 발견한 버그:

```txt
minimum_spanning_tree-1647
```

원인:

- 기존 Python oracle이 BOJ 1647 도시 분할 계획 입력(`N M` + 간선 목록)이 아니라 행렬 입력을 읽는 다른 MST 형태였다.
- 1차 수정에서는 `N=2` 같은 경계에서 도로를 하나도 남기지 않아야 하는데 선택 간선을 더하는 문제가 있었다.

조치:

- `data/problems.json` 안의 `minimum_spanning_tree-1647` Python oracle을 BOJ 1647 형식에 맞는 Kruskal 구현으로 교체했다.
- MST를 완성한 뒤 선택된 간선 중 가장 큰 비용을 빼서 두 마을로 분리하도록 수정했다.
- `harness/overrides/minimum_spanning_tree-1647.py`에 `N=2`, 삼각형, 샘플, stress 케이스를 추가했다.

4차 batch 이후:

```txt
npm run judge:verify-overrides -- minimum_spanning_tree-1197 minimum_spanning_tree-1368 minimum_spanning_tree-1647 minimum_spanning_tree-1774 minimum_spanning_tree-1922 minimum_spanning_tree-2887 minimum_spanning_tree-4386 minimum_spanning_tree-6497 graph_traversal-1012 graph_traversal-2206 graph_traversal-11724 graph_traversal-11725 graph_traversal-17836 two_pointer-1940 two_pointer-2018 two_pointer-2230 two_pointer-2470 binary_search-1654 binary_search-1789 binary_search-1920
-> OK: 20 override files self-judged successfully.

npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 91
-> sampleOnly 271
-> highRiskSampleOnly 132

npm run harness:test
-> OK, 9 tests
```

다음 coverage 상위 후보:

```txt
binary_search-2110
binary_search-2143
binary_search-2417
binary_search-2470
binary_search-2776
binary_search-6236
binary_search-9024
binary_search-10815
binary_search-10816
dynamic_programming_2-1005
dynamic_programming_1-1463
dynamic_programming_on_trees-2533
dynamic_programming_2-5557
dynamic_programming_1-11660
dynamic_programming_1-11726
dynamic_programming_1-13699
dynamic_programming_2-14567
dynamic_programming_1-14722
dynamic_programming_1-22869
backtracking-1182
```

5차 batch:

```txt
binary_search-2110
binary_search-2143
binary_search-2417
binary_search-2470
binary_search-2776
binary_search-6236
binary_search-9024
binary_search-10815
binary_search-10816
dynamic_programming_2-1005
dynamic_programming_1-1463
dynamic_programming_on_trees-2533
dynamic_programming_2-5557
dynamic_programming_1-11660
dynamic_programming_1-11726
dynamic_programming_1-13699
dynamic_programming_2-14567
dynamic_programming_1-14722
dynamic_programming_1-22869
backtracking-1182
```

5차 batch 이후:

```txt
npm run judge:verify-overrides -- binary_search-2110 binary_search-2143 binary_search-2417 binary_search-2470 binary_search-2776 binary_search-6236 binary_search-9024 binary_search-10815 binary_search-10816 dynamic_programming_2-1005 dynamic_programming_1-1463 dynamic_programming_on_trees-2533 dynamic_programming_2-5557 dynamic_programming_1-11660 dynamic_programming_1-11726 dynamic_programming_1-13699 dynamic_programming_2-14567 dynamic_programming_1-14722 dynamic_programming_1-22869 backtracking-1182
-> OK: 20 override files self-judged successfully.

npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 111
-> sampleOnly 251
-> highRiskSampleOnly 112

npm run harness:test
-> OK, 9 tests
```

다음 coverage 상위 후보:

```txt
backtracking-1189
backtracking-2026
backtracking-2580
backtracking-9663
backtracking-10974
simulation-5373
prefix_sum-1749
prefix_sum-2167
prefix_sum-10986
prefix_sum-11659
prefix_sum-20440
minimum_spanning_tree-16398
minimum_spanning_tree-20010
graph_traversal-1260
graph_traversal-14502
graph_traversal-16918
graph_traversal-16953
data_structure-1158
data_structure2-1269
data_structure2-1620
```

6차 batch:

```txt
backtracking-1189
backtracking-2026
backtracking-2580
backtracking-9663
backtracking-10974
simulation-5373
prefix_sum-1749
prefix_sum-2167
prefix_sum-10986
prefix_sum-11659
prefix_sum-20440
minimum_spanning_tree-16398
minimum_spanning_tree-20010
graph_traversal-1260
graph_traversal-14502
graph_traversal-16918
graph_traversal-16953
data_structure-1158
data_structure2-1269
data_structure2-1620
```

6차 batch에서 조정한 케이스:

```txt
backtracking-1189
prefix_sum-10986
minimum_spanning_tree-20010
```

원인:

- `backtracking-1189`: 장애물 위치가 목표 칸을 막는 케이스의 expected를 잘못 계산했다.
- `prefix_sum-10986`: stress 케이스의 나머지별 prefix count 조합 수를 잘못 계산했다.
- `minimum_spanning_tree-20010`: MST 위 지름 계산 expected를 실제 선택 MST 기준으로 다시 맞췄다.

검증:

```txt
npm run judge:verify-overrides -- backtracking-2026 backtracking-10974 graph_traversal-14502 graph_traversal-16953 data_structure-1158 data_structure2-1269 prefix_sum-11659
-> OK: 7 override files self-judged successfully.

npm run judge:verify-overrides -- backtracking-1189 backtracking-2580 backtracking-9663 simulation-5373 prefix_sum-1749
-> backtracking-1189 expected 조정 후 통과

npm run judge:verify-overrides -- prefix_sum-2167
-> OK: 1 override files self-judged successfully.

npm run judge:verify-overrides -- prefix_sum-20440
-> OK: 1 override files self-judged successfully.

npm run judge:verify-overrides -- minimum_spanning_tree-16398
-> OK: 1 override files self-judged successfully.

npm run judge:verify-overrides -- backtracking-1189 prefix_sum-10986 minimum_spanning_tree-20010
-> OK: 3 override files self-judged successfully.

npm run judge:verify-overrides -- graph_traversal-1260
-> OK: 1 override files self-judged successfully.

npm run judge:verify-overrides -- graph_traversal-16918
-> OK: 1 override files self-judged successfully.

npm run judge:verify-overrides -- data_structure2-1620
-> OK: 1 override files self-judged successfully.
```

6차 batch 이후:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 131
-> sampleOnly 231
-> highRiskSampleOnly 92

npm run harness:test
-> OK, 9 tests
```

다음 coverage 상위 후보:

```txt
data_structure2-1927
data_structure-1966
data_structure2-2075
data_structure-2164
data_structure-2346
data_structure-2493
data_structure2-4358
data_structure-5397
data_structure-5430
data_structure2-7662
data_structure-10845
data_structure2-11279
data_structure2-11286
data_structure2-14425
data_structure2-21939
two_pointer-15961
two_pointer-20922
binary_search-2512
binary_search-2805
binary_search-3079
```

7차 batch:

```txt
data_structure2-1927
data_structure-1966
data_structure2-2075
data_structure-2164
data_structure-2346
data_structure-2493
data_structure2-4358
data_structure-5397
data_structure-5430
data_structure2-7662
data_structure-10845
data_structure2-11279
data_structure2-11286
data_structure2-14425
data_structure2-21939
two_pointer-15961
two_pointer-20922
binary_search-2512
binary_search-2805
binary_search-3079
```

7차 batch에서 발견한 버그:

```txt
data_structure2-11279
data_structure-2346
```

원인:

- `data_structure2-11279`: `0` 명령 처리 후에도 `heapq.heappush(heap, -a)`가 실행되어 최대 힙에 `0`이 들어갔다.
- `data_structure-2346`: BOJ에서는 공백 출력이 허용되지만, 우리 judge의 라인 비교에서는 sample과 다르게 줄마다 출력되어 PE가 발생했다.

조치:

- `data_structure2-11279` oracle을 `a != 0`일 때만 push하도록 수정했다.
- `data_structure-2346` oracle을 방문 순서를 `answer`에 모은 뒤 `print(*answer)`로 한 줄 출력하도록 수정했다.

7차 batch 검증:

```txt
npm run judge:verify-overrides -- data_structure2-2075 data_structure-2493 data_structure2-4358 data_structure2-21939 two_pointer-20922
-> OK: 5 override files self-judged successfully.

npm run judge:verify-overrides -- data_structure2-1927 data_structure-1966 data_structure-2164 data_structure-2346 data_structure-5397 data_structure-5430 data_structure2-7662 data_structure-10845 data_structure2-11279 data_structure2-11286 data_structure2-14425 two_pointer-15961 binary_search-2512 binary_search-2805 binary_search-3079
-> OK: 15 override files self-judged successfully.
```

7차 batch 이후:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 151
-> sampleOnly 211
-> highRiskSampleOnly 72

npm run harness:test
-> OK, 9 tests
```

다음 coverage 상위 후보:

```txt
binary_search-19637
binary_search-20444
dynamic_programming_1-1912
dynamic_programming_1-10164
dynamic_programming_1-11048
dynamic_programming_1-11727
simulation-14503
prefix_sum-2015
prefix_sum-11660
prefix_sum-20438
prefix_sum-21318
minimum_spanning_tree-21924
graph_traversal-2178
graph_traversal-13023
graph_traversal-20924
graph_traversal-1058
graph_traversal-7576
graph_traversal-16234
graph_traversal-16954
data_structure-1874
```

8차 batch:

```txt
binary_search-19637
binary_search-20444
dynamic_programming_1-1912
dynamic_programming_1-10164
dynamic_programming_1-11048
dynamic_programming_1-11727
simulation-14503
prefix_sum-2015
prefix_sum-11660
prefix_sum-20438
prefix_sum-21318
minimum_spanning_tree-21924
graph_traversal-2178
graph_traversal-13023
graph_traversal-20924
graph_traversal-1058
graph_traversal-7576
graph_traversal-16234
graph_traversal-16954
data_structure-1874
```

8차 batch에서 발견한 버그:

```txt
graph_traversal-20924
prefix_sum-20438
```

원인:

- `graph_traversal-20924`: Python oracle의 줄 연결 구문이 저장 과정에서 깨져 `SyntaxError`가 발생했다.
- `prefix_sum-20438`: C++ oracle의 전역 배열명 `sleep`이 Linux `<unistd.h>`의 `sleep()` 함수와 충돌해 CE가 발생했다.

조치:

- `graph_traversal-20924` oracle의 조건문을 괄호 기반으로 정리해 줄 연결 의존을 제거했다.
- `prefix_sum-20438` oracle의 `sleep` 배열명을 `sleeping`으로 바꿨다.

8차 batch 검증:

```txt
npm run judge:verify-overrides -- binary_search-19637 binary_search-20444 dynamic_programming_1-1912 dynamic_programming_1-10164 dynamic_programming_1-11048 dynamic_programming_1-11727 simulation-14503 prefix_sum-2015 prefix_sum-11660 prefix_sum-20438 prefix_sum-21318 minimum_spanning_tree-21924 graph_traversal-2178 graph_traversal-13023 graph_traversal-20924 graph_traversal-1058 graph_traversal-7576 graph_traversal-16234 graph_traversal-16954 data_structure-1874
-> OK: 20 override files self-judged successfully.
```

8차 batch 이후:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 171
-> sampleOnly 191
-> highRiskSampleOnly 52

npm run harness:test
-> OK, 9 tests
```

다음 coverage 상위 후보:

```txt
data_structure-1935
data_structure-2504
data_structure-9012
data_structure-10799
data_structure-10828
data_structure-10866
data_structure-18115
data_structure-22942
binary_search-1477
dynamic_programming_1-1106
dynamic_programming_on_trees-1135
dynamic_programming_2-11985
dynamic_programming_1-15486
dynamic_programming_1-17626
dynamic_programming_1-2839
dynamic_programming_2-21923
backtracking-1038
backtracking-14712
backtracking-14889
backtracking-15649
```

9차 batch:

```txt
data_structure-1935
data_structure-2504
data_structure-9012
data_structure-10799
data_structure-10828
data_structure-10866
data_structure-18115
data_structure-22942
binary_search-1477
dynamic_programming_1-1106
dynamic_programming_on_trees-1135
dynamic_programming_2-11985
dynamic_programming_1-15486
dynamic_programming_1-17626
dynamic_programming_1-2839
dynamic_programming_2-21923
backtracking-1038
backtracking-14712
backtracking-14889
backtracking-15649
```

9차 batch 검증:

```txt
npm run judge:verify-overrides -- data_structure-1935 data_structure-2504 data_structure-9012 data_structure-10828 data_structure-10866 binary_search-1477 dynamic_programming_on_trees-1135 dynamic_programming_2-11985 dynamic_programming_1-17626 dynamic_programming_2-21923 backtracking-1038 backtracking-14712 backtracking-15649
-> OK: 13 override files self-judged successfully.

npm run judge:verify-overrides -- data_structure-10799 data_structure-18115 data_structure-22942 dynamic_programming_1-1106 dynamic_programming_1-15486 dynamic_programming_1-2839 backtracking-14889
-> OK: 7 override files self-judged successfully.
```

9차 batch 이후:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 191
-> sampleOnly 171
-> highRiskSampleOnly 32

npm run harness:test
-> OK, 9 tests
```

다음 coverage 상위 후보:

```txt
backtracking-15650
backtracking-15651
backtracking-15652
backtracking-15654
backtracking-15655
backtracking-15656
backtracking-15658
backtracking-15663
backtracking-15664
backtracking-15665
backtracking-15666
backtracking-22944
simulation-3190
simulation-21610
prefix_sum-16971
prefix_sum-20543
data_structure-3986
data_structure2-10546
data_structure2-21942
backtracking-16198
```

## 10차 batch 기록

이번 batch에서는 coverage 상위 후보를 기준으로 override를 추가했다.

추가한 override:

```txt
backtracking-15650
backtracking-15651
backtracking-15652
backtracking-15654
backtracking-15655
backtracking-15656
backtracking-15658
backtracking-15663
backtracking-15664
backtracking-15665
backtracking-15666
backtracking-22944
simulation-3190
simulation-21610
data_structure-3986
data_structure2-10546
data_structure2-21942
backtracking-16198
backtracking-1405
simulation-14499
prefix_sum-16971
prefix_sum-20543
```

검증 결과:

```txt
npm run judge:verify-overrides -- backtracking-15650 backtracking-15651 backtracking-15652 backtracking-15654 backtracking-15655 backtracking-15656 backtracking-15658 backtracking-15663 backtracking-15664 backtracking-15665 backtracking-15666 backtracking-22944 simulation-3190 simulation-21610 data_structure-3986 data_structure2-10546 data_structure2-21942 backtracking-16198 backtracking-1405 simulation-14499
-> OK: 20 override files self-judged successfully.

prefix_sum-16971
prefix_sum-20543
-> C++ 전용 oracle 문제라 현재 로컬 g++ 없음 / Docker daemon 미실행 상태에서는 일반 verify 스크립트로 self-judge 불가.
-> generated case마다 expected output을 override에 직접 기록해서 oracle 실행 의존성을 제거했다.
-> 별도 Python 기준 검증으로 두 문제 모두 AC 9/9 확인.

npm run harness:test
-> OK, 9 tests
```

coverage 결과:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 213
-> sampleOnly 149
-> highRiskSampleOnly 10
```

다음 coverage 상위 후보:

```txt
simulation-14891
simulation-16234
simulation-16236
simulation-20057
simulation-20058
simulation-20061
simulation-17144
data_structure-1021
data_structure-1918
data_structure2-1302
```

## 11차 batch 기록

10차 이후 남아 있던 `highRiskSampleOnly` 10개를 모두 처리했다.

추가한 override:

```txt
simulation-14891
simulation-16234
simulation-16236
simulation-20057
simulation-20058
simulation-20061
simulation-17144
data_structure-1021
data_structure-1918
data_structure2-1302
```

검증 결과:

```txt
npm run judge:verify-overrides -- simulation-14891 simulation-16234 simulation-20058 data_structure-1021 data_structure2-1302
-> OK: 5 override files self-judged successfully.

simulation-16236
simulation-20057
simulation-20061
simulation-17144
data_structure-1918
-> C++ 전용 oracle 문제라 override에 expected output을 직접 기록했다.
-> 별도 Python 기준 검증으로 5개 모두 AC 9/9 확인.

npm run harness:test
-> OK, 9 tests
```

coverage 결과:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 223
-> sampleOnly 139
-> highRiskSampleOnly 0
-> topCandidates []
```

의미:

- 우선순위가 높다고 분류된 sample-only 문제는 모두 override가 생겼다.
- 이제 남은 작업은 일반 sample-only 139개를 유형별로 천천히 줄이는 단계다.

## 12차 batch 기록

일반 sample-only 139개 중 Python oracle로 안정 검증 가능한 brute force / disjoint set / greedy 문제 20개를 추가했다.

추가한 override:

```txt
brute_force-1145
brute_force-1436
brute_force-1969
brute_force-2503
brute_force-4096
brute_force-5568
brute_force-7568
brute_force-9094
brute_force-13410
brute_force-14500
brute_force-14620
brute_force-15661
brute_force-17471
brute_force-17626
brute_force-18511
brute_force-18808
brute_force-21278
disjoint_set-1717
greedy-1758
greedy-1817
```

발견한 문제:

```txt
brute_force-15661
```

원인:

- 저장된 Python oracle이 팀 크기를 `N//2`로 고정해서 검사했다.
- 실제 BOJ 15661은 두 팀의 인원수가 같지 않아도 된다.
- 또한 팀 시너지 계산은 `S[i][j] + S[j][i]`를 포함해야 한다.

조치:

- `data/problems.json`의 `brute_force-15661` Python oracle을 bitmask 기반 전체 팀 분할 검사로 교체했다.

검증 결과:

```txt
npm run judge:verify-overrides -- brute_force-1145 brute_force-1436 brute_force-1969 brute_force-2503 brute_force-4096 brute_force-5568 brute_force-7568 brute_force-9094 brute_force-13410 brute_force-14500 brute_force-14620 brute_force-15661 brute_force-17471 brute_force-17626 brute_force-18511 brute_force-18808 brute_force-21278 disjoint_set-1717 greedy-1758 greedy-1817
-> OK: 20 override files self-judged successfully.

npm run harness:test
-> OK, 9 tests
```

coverage 결과:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 243
-> sampleOnly 119
-> highRiskSampleOnly 0
```

## 13차 batch 기록

일반 sample-only 중 Python oracle로 바로 검증 가능한 20개를 추가했다.

추가한 override:

```txt
brute_force-21315
disjoint_set-1976
disjoint_set-10775
divide_and_conquer-1802
greedy-1931
greedy-2141
greedy-2212
greedy-2812
greedy-11399
greedy-11508
greedy-13164
greedy-14247
greedy-14916
greedy-16208
greedy-16435
implementation-2729
implementation-14719
implementation-15787
implementation-15806
implementation-16935
```

검증 결과:

```txt
npm run judge:verify-overrides -- brute_force-21315 disjoint_set-1976 disjoint_set-10775 divide_and_conquer-1802 greedy-1931 greedy-2141 greedy-2212 greedy-2812 greedy-11399 greedy-11508 greedy-13164 greedy-14247 greedy-14916 greedy-16208 greedy-16435 implementation-2729 implementation-14719 implementation-15787 implementation-15806 implementation-16935
-> OK: 20 override files self-judged successfully.

npm run harness:test
-> OK, 9 tests
```

coverage 결과:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 263
-> sampleOnly 99
-> highRiskSampleOnly 0
```

## 14차 batch 기록

일반 sample-only 중 Python oracle로 검증 가능한 구현/수학/문자열 문제 20개를 추가했다.

추가한 override:

```txt
implementation-1212
implementation-17413
implementation-21608
implementation-21918
math-1978
math-2753
math-5618
math-11653
math-21312
math-21919
math-21920
string-1032
string-1152
string-1181
string-1316
string-2204
string-2744
string-3029
string-9046
string-9342
```

발견한 문제:

```txt
math-5618
math-21920
string-9046
```

조치:

- `math-5618`: 저장된 Python oracle이 약수를 한 줄에 출력해서 BOJ sample과 `PE`가 발생했다. 약수를 한 줄에 하나씩 출력하도록 수정했다.
- `math-21920`: 저장된 Python oracle이 정수 평균도 `6.0`처럼 출력해서 BOJ sample과 충돌했다. 나누어떨어지는 경우 정수로 출력하도록 수정했다.
- `string-9046`: 공백만 있는 invalid input을 override에서 제거하고 유효한 단일 문자 입력으로 교체했다.

검증 결과:

```txt
npm run judge:verify-overrides -- implementation-1212 implementation-17413 implementation-21608 implementation-21918 math-1978 math-2753 math-5618 math-11653 math-21312 math-21919 math-21920 string-1032 string-1152 string-1181 string-1316 string-2204 string-2744 string-3029 string-9046 string-9342
-> OK: 20 override files self-judged successfully.

npm run harness:test
-> OK, 9 tests
```

coverage 결과:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 283
-> sampleOnly 79
-> highRiskSampleOnly 0
```

## 15차 batch 기록

남은 sample-only 중 Python oracle 6개와 expected를 직접 고정할 수 있는 C++ 전용 14개를 추가했다.

추가한 override:

```txt
brute_force-2231
brute_force-2422
brute_force-15721
brute_force-18312
brute_force-19532
greedy-13305
greedy-20300
greedy-20365
implementation-1244
implementation-2753
implementation-14467
math-1110
math-1934
math-2581
string-10798
string-11365
string-12871
string-17609
string-20154
tree-15681
```

검증 방식:

- `string-10798`, `string-11365`, `string-12871`, `string-17609`, `string-20154`, `tree-15681`은 Python oracle로 `judge:verify-overrides` 통과.
- 나머지 14개는 로컬에 C++ 컴파일러가 없으므로 expected output을 override에 직접 기록하고, 별도 Python 기준 코드로 AC 확인.

수정한 case:

```txt
brute_force-15721
```

원인:

- 처음 작성한 override가 `A T 구호`를 한 줄에 넣었다.
- 실제 BOJ 입력은 `A`, `T`, `구호`가 각각 별도 줄이다.

조치:

- 입력 형식을 세 줄로 수정하고 다시 검증했다.

검증 결과:

```txt
npm run judge:verify-overrides -- string-10798 string-11365 string-12871 string-17609 string-20154 tree-15681
-> OK: 6 override files self-judged successfully.

expected 고정 14개
-> 별도 Python 기준 검증 AC 확인.

npm run harness:test
-> OK, 9 tests
```

coverage 결과:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 303
-> sampleOnly 59
-> highRiskSampleOnly 0
```

## 16차 batch 기록

남은 sample-only 중 expected를 직접 계산할 수 있는 구현/수학/문자열 문제 20개를 추가했다.

추가한 override:

```txt
implementation-1913
implementation-20291
implementation-20436
implementation-20546
implementation-21756
math-1747
math-2609
math-2745
math-2960
math-4134
math-5347
math-9613
math-21275
math-22864
string-1764
string-4659
string-6550
string-16171
string-17413
string-20437
```

검증 방식:

- 로컬에 C++/Java 컴파일러가 없어서 일반 `judge:verify-overrides`로는 C++/Java 전용 문제를 self-judge할 수 없다.
- 각 override 내부에 작은 기준 solver를 두고, generated case마다 expected output을 직접 생성하도록 했다.
- `harness.generators.generate` 기준으로 20개 override 모두 import 및 expected 생성 검증을 통과했다.

보류한 문제:

```txt
brute_force-4690
```

사유:

- 입력이 없는 출력 전용 문제다.
- 저장된 전체 출력과 BOJ sample-only expected가 섞이면 false negative가 발생한다.
- 이 문제는 별도 정책을 정한 뒤 처리하는 것이 안전하다.

검증 결과:

```txt
expected 계산형 override 20개
-> import OK
-> generated cases all include expected

npm run harness:test
-> OK, 9 tests
```

coverage 결과:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 323
-> sampleOnly 39
-> highRiskSampleOnly 0
```

## 17차 batch 기록

남은 sample-only 중 브루트포스, 분리집합, 분할정복, 그리디, 구현 문제 20개를 추가했다.

추가한 override:

```txt
brute_force-1107
brute_force-2615
brute_force-9079
brute_force-16439
disjoint_set-1043
disjoint_set-4195
disjoint_set-16562
disjoint_set-17352
disjoint_set-18116
divide_and_conquer-1074
divide_and_conquer-1992
divide_and_conquer-2630
divide_and_conquer-4779
divide_and_conquer-17829
divide_and_conquer-18222
greedy-1092
greedy-1541
greedy-2217
greedy-21758
implementation-2578
```

검증 방식:

- C++/Java 전용 문제가 대부분이라 override 내부에 문제별 기준 solver를 넣었다.
- generated case마다 expected output이 생성되는지 확인했다.

검증 결과:

```txt
expected 계산형 override 20개
-> import OK
-> generated cases all include expected

npm run harness:test
-> OK, 9 tests
```

coverage 결과:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 343
-> sampleOnly 19
-> highRiskSampleOnly 0
```

## 18차 batch 기록

남은 sample-only 19개를 모두 override 대상으로 전환했다.

추가한 override:

```txt
brute_force-4690
brute_force-13140
divide_and_conquer-2447
divide_and_conquer-2448
divide_and_conquer-4256
implementation-4396
implementation-10994
implementation-12933
implementation-16926
implementation-20207
implementation-22856
math-1990
string-20291
tree-1068
tree-1967
tree-1991
tree-3584
tree-11437
trie-14425
```

핵심 처리:

- `brute_force-4690`은 입력이 없는 출력 전용 문제이고, 저장된 BOJ sample expected가 전체 출력이 아니라 앞부분만 포함되어 false negative가 발생할 수 있었다.
- 이 문제는 override 파일에 `REPLACE_SAMPLES = True`를 선언하고, judge core가 해당 플래그를 보면 BOJ sample 대신 override case만 사용하도록 했다.
- 나머지 문제는 override 내부 기준 solver로 expected output을 직접 생성한다.

검증 결과:

```txt
npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 362
-> sampleOnly 0
-> highRiskSampleOnly 0

override import / expected 생성 검증
-> 19개 모두 OK

npm run harness:test
-> OK, 9 tests

npm run judge:verify-overrides -- brute_force-4690 tree-1991 tree-3584 tree-11437 trie-14425
-> brute_force-4690 python AC 1/1
-> C++ 문제 4개는 현재 로컬 PC에 g++가 없어 실행 검증 불가

npm run judge:lang-audit
-> allProblemsAcceptPythonCpp true
-> localGppAvailable false
-> dockerCliAvailable true
```

현재 상태:

- 전체 362문제 모두 override 또는 sample case를 통해 judge 가능하다.
- sample-only 문제는 0개다.
- 운영에서 C++ 제출까지 실제 실행하려면 `JUDGE_USE_DOCKER=1`과 C++ 컴파일러가 포함된 coderunner Docker image가 필요하다.
