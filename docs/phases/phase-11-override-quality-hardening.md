# Phase 11. Override 품질 보강

## 목표

`judge:quality` 기준으로 남아 있던 저품질 override를 제거한다.

## 작업 내용

- expected가 없던 핵심 문제는 override 내부 solver를 추가했다.
- 가장 큰 기존 케이스가 `edge`로만 표시된 문제는 의미에 맞게 `stress`로 승격했다.
- `brute_force-4690`은 입력이 없는 출력 전용 exhaustive 문제이므로 `QUALITY_EXCEPTION`을 명시했다.

## 보강 대상

대표적으로 다음 문제들을 보강했다.

```txt
brute_force-2798
backtracking-15657
backtracking-22944
brute_force-2309
data_structure-2800
graph_traversal-16174
implementation-5597
simulation-3190
tree-11437
tree-1991
tree-3584
trie-14425
divide_and_conquer-2447
backtracking-18430
dynamic_programming_1-10870
dynamic_programming_1-11055
dynamic_programming_1-15989
dynamic_programming_1-15990
dynamic_programming_1-1890
dynamic_programming_1-21317
dynamic_programming_2-1516
dynamic_programming_2-7579
dynamic_programming_on_trees-15681
dynamic_programming_on_trees-1949
dynamic_programming_on_trees-2213
graph_traversal-14940
graph_traversal-2573
graph_traversal-2606
graph_traversal-2636
graph_traversal-2667
graph_traversal-5547
graph_traversal-9328
minimum_spanning_tree-14621
prefix_sum-21757
simulation-20165
```

## 검증 결과

```txt
npm run judge:quality
-> total 362
-> averageQualityScore 80.28
-> lowQualityCount 0
-> missingStressCount 0
-> allHaveOverride true

npm run harness:test
-> OK, 14 tests

npm run judge:coverage
-> total 362
-> judgeReady 362
-> missingCases 0
-> overrides 362
-> sampleOnly 0
-> highRiskSampleOnly 0
```

## 판단

- 전체 `npm run judge:verify-overrides`는 이미 통과 이력이 있다.
- 이번 변경분은 묶음별 `npm run judge:verify-overrides -- ...`로 self-judge를 확인했다.
- 전체 Docker 검증은 시간이 길기 때문에 nightly workflow에서 반복 검증한다.
