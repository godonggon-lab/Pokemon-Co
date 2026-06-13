# Phase 70 - Low Case Count Hardening Batch 17

## 목표

`graph_traversal-18352`부터 `graph_traversal-3055`까지
20개 override의 입력 케이스를 최소 6개로 보강한다.

## 처리한 문제

- `graph_traversal-18352`
- `graph_traversal-18404`
- `graph_traversal-18405`
- `graph_traversal-1926`
- `graph_traversal-2146`
- `graph_traversal-2151`
- `graph_traversal-21937`
- `graph_traversal-21938`
- `graph_traversal-2194`
- `graph_traversal-2234`
- `graph_traversal-22868`
- `graph_traversal-22946`
- `graph_traversal-22948`
- `graph_traversal-22949`
- `graph_traversal-2583`
- `graph_traversal-2638`
- `graph_traversal-2644`
- `graph_traversal-2665`
- `graph_traversal-2668`
- `graph_traversal-3055`

## 구현 내용

- 최단거리 BFS에는 시작과 목적지가 같은 경우, 도달 불가, 같은 거리의 여러 정점을 추가했다.
- 격자 탐색에는 전체 빈 칸, 전체 연결, 대각선 분리와 여러 컴포넌트를 보강했다.
- 다중 시작 전파에는 바이러스 우선순위와 물 확산 시점이 결과를 바꾸는 입력을 추가했다.
- 섬과 다리 문제에는 인접 섬, 멀리 떨어진 섬과 여러 섬 사이 최단 연결을 추가했다.
- 치즈 문제에는 단일 치즈, 작은 정사각형과 내부 공기 공간을 포함한 입력을 보강했다.
- 고정 기대값 문제는 reference solution으로 실제 출력을 확인하고 잘못 계산한 기대값을 교정했다.

## 검증 중 바로잡은 사항

- `22868`은 왕복 경로가 존재해야 하므로 단절 또는 단일 경로 입력을 순환 경로 입력으로 교체했다.
- `21938`은 RGB 평균값이 임계값 이상인 픽셀만 컴포넌트에 포함하도록 기대값을 수정했다.
- `2234`는 벽 비트 방향과 방 병합 크기를 reference 결과에 맞춰 재검산했다.
- `22946`, `22948`은 원의 포함 트리에서 가상 루트가 경로에 미치는 영향을 반영했다.
- `3055`는 비버 굴에는 물이 퍼지지 않는 규칙을 반영해 기대값을 수정했다.

## 검증 결과

```text
override self-judge: 20개 모두 AC
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 83.81
lowQualityCount: 252
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `272 -> 252`로 감소했다.
- 평균 품질 점수가 `83.32 -> 83.81`로 상승했다.
- 다음 일반 배치는 `graph_traversal-5427`부터 진행한다.
