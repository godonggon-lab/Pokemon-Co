# Phase 69 - Low Case Count Hardening Batch 16

## 목표

`graph_traversal-14442`부터 `graph_traversal-17616`까지
20개 override의 입력 케이스를 최소 6개로 보강한다.

## 처리한 문제

- `graph_traversal-14442`
- `graph_traversal-14496`
- `graph_traversal-14923`
- `graph_traversal-15558`
- `graph_traversal-1600`
- `graph_traversal-16432`
- `graph_traversal-16928`
- `graph_traversal-16932`
- `graph_traversal-16947`
- `graph_traversal-16948`
- `graph_traversal-16956`
- `graph_traversal-16973`
- `graph_traversal-16985`
- `graph_traversal-16988`
- `graph_traversal-17086`
- `graph_traversal-17129`
- `graph_traversal-17141`
- `graph_traversal-17142`
- `graph_traversal-1743`
- `graph_traversal-17616`

## 구현 내용

- 벽 부수기와 특수 이동 BFS에는 자원 0개, 자원 소진, 도달 불가능 입력을 추가했다.
- 상태 전파 문제에는 시작과 목표가 같은 경우, 다중 시작점, 완전 차단 입력을 보강했다.
- 사이클 거리에는 순수 사이클과 길이가 다른 가지가 연결된 그래프를 추가했다.
- 격자 컴포넌트 문제에는 전체 빈 칸, 전체 채움, 분리 영역과 합쳐지는 영역을 추가했다.
- 고정 크기 3차원 미로에는 중앙 또는 모서리 일부가 막힌 유효 보드를 생성식으로 추가했다.
- 바이러스 선택 문제에는 빈 칸이 없는 경우와 단일 바이러스 전파 입력을 보강했다.

## 검증 중 바로잡은 사항

- `14496`: 첫 줄은 시작·목표 정점, 둘째 줄은 정점·간선 수이므로 잘못 구성한 입력 순서를 수정했다.
- `16948`: 데스 나이트 이동 규칙상 도달할 수 없는 좌표의 기대값을 `-1`로 수정했다.
- `16988`: 상대 돌을 포획하려면 모든 자유도를 두 수로 막아야 하므로 보드 구성을 수정했다.
- `17616`: 순위 범위의 두 번째 값은 아래 학생 수를 제외한 최저 순위이므로 기대값을 수정했다.

## 검증 결과

```text
override self-judge: 20개 모두 python AC 6/6
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 83.32
lowQualityCount: 272
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `292 -> 272`로 감소했다.
- 평균 품질 점수가 `82.82 -> 83.32`로 상승했다.
- 다음 일반 배치는 `graph_traversal-18352`부터 진행한다.
