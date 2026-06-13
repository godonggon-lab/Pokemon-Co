# Phase 72 - 저빈도 케이스 보강 배치 19

## 목표

`minimum_spanning_tree-13905`부터 `shortest_path-11780`까지
20개 override의 입력 케이스를 최소 6개로 보강한다.

## 처리한 문제

- `minimum_spanning_tree-13905`
- `minimum_spanning_tree-14950`
- `minimum_spanning_tree-16202`
- `minimum_spanning_tree-17472`
- `minimum_spanning_tree-17490`
- `minimum_spanning_tree-18769`
- `minimum_spanning_tree-1944`
- `minimum_spanning_tree-2406`
- `prefix_sum-17123`
- `prefix_sum-17390`
- `prefix_sum-20116`
- `prefix_sum-20159`
- `prefix_sum-3673`
- `prefix_sum-5549`
- `shortest_path-10159`
- `shortest_path-11403`
- `shortest_path-11404`
- `shortest_path-11657`
- `shortest_path-11779`
- `shortest_path-11780`

## 구현 내용

- MST 문제에 단일 간선, 연결 불가, 다중 경로, 게임 후반 MST 실패와 섬 사이 최소 다리 길이 케이스를 추가했다.
- 격자 MST와 키 수집 문제에 한 칸 격자, 일렬 격자, 장애물 우회 및 여러 키 연결 케이스를 추가했다.
- 누적 합 문제에 단일 원소, 음수 갱신, 중복 값, 0으로만 구성된 입력과 부분 직사각형 질의를 추가했다.
- 최단 경로 문제에 연결되지 않은 정점, 중복 간선, 음수 간선, 도달 불가능한 음수 사이클과 경로 복원 케이스를 추가했다.
- 경로 출력 문제는 최단 경로 동률이 발생하지 않도록 입력을 구성했다.

## reference 출력으로 교정한 항목

- `minimum_spanning_tree-16202`: 세 번째 라운드에서 MST가 성립하지 않는 결과를 0으로 교정했다.
- `minimum_spanning_tree-17472`: 다리 길이는 섬 사이 바다 칸 수이며, 연결되지 않는 섬 배치는 `-1`로 교정했다.
- `minimum_spanning_tree-17490`: 끊어진 원형 간선과 우물 비용을 반영해 예산 초과 결과를 `NO`로 교정했다.
- `minimum_spanning_tree-18769`: 2x3 격자의 모든 정점을 연결하는 비용을 22로 교정했다.
- `minimum_spanning_tree-1944`: 키 사이 최단 거리와 MST 합계를 각각 4, 10으로 교정했다.
- `prefix_sum-20116`: 중심점 조건을 만족하지 않는 증가 수열을 `unstable`로 교정했다.

## 검증 결과

```text
override self-judge: 20개 모두 AC (각 6/6)
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 84.80
lowQualityCount: 212
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `232 -> 212`로 감소했다.
- 평균 품질 점수가 `84.31 -> 84.80`으로 상승했다.
- 다음 일반 배치는 `shortest_path-1219`부터 진행한다.
