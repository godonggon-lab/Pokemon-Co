# Phase 71 - 저빈도 케이스 보강 배치 18

## 목표

`graph_traversal-5427`부터 `minimum_spanning_tree-13418`까지
20개 override의 입력 케이스를 최소 6개로 보강한다.

## 처리한 문제

- `graph_traversal-5427`
- `graph_traversal-6087`
- `graph_traversal-6118`
- `graph_traversal-7562`
- `graph_traversal-9019`
- `graph_traversal-9466`
- `greedy-13019`
- `greedy-13975`
- `greedy-19539`
- `greedy-20117`
- `greedy-2109`
- `greedy-21313`
- `greedy-21314`
- `greedy-2285`
- `greedy-2457`
- `greedy-8980`
- `math-1359`
- `minimum_spanning_tree-10423`
- `minimum_spanning_tree-1045`
- `minimum_spanning_tree-13418`

## 구현 내용

- 그래프 탐색 문제에 시작점과 도착점의 특수 위치, 동률 최장 거리, 순환 및 비순환 함수 그래프를 추가했다.
- 불 탈출과 레이저 통신에는 즉시 탈출, 완전 봉쇄, 우회 경로 및 거울 수 변화 케이스를 추가했다.
- 그리디 문제에는 동일 값, 동률 우선순위, 불가능 구간, 완전 중첩 구간과 용량 재사용 케이스를 추가했다.
- 수학 확률 문제에는 교집합 조건이 0인 경우, 전체 선택, 단일 선택을 추가했다.
- MST 문제에는 다중 발전소, 최소 간선 수, 완전 그래프, 연결 불가와 오르막 간선 수 차이를 추가했다.

## reference 출력으로 교정한 항목

- `greedy-13019`: `AABC -> ABCA` 변환의 최소 이동 횟수를 3으로 교정했다.
- `greedy-20117`: 동일 품질 네 개의 최종 품질 합을 10으로 교정했다.
- `greedy-2457`: 중첩 꽃 구간에서 최장 종료일을 선택하면 두 개로 전체 기간을 덮는 결과를 반영했다.

## 검증 결과

```text
override self-judge: 20개 모두 AC (각 6/6)
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 84.31
lowQualityCount: 232
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `252 -> 232`로 감소했다.
- 평균 품질 점수가 `83.81 -> 84.31`로 상승했다.
- 다음 일반 배치는 `minimum_spanning_tree-13905`부터 진행한다.

