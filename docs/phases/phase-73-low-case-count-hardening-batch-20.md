# Phase 73 - 저빈도 케이스 보강 배치 20

## 목표

`shortest_path-1219`부터 `shortest_path-21940`까지
최단 경로 override 20개의 입력 케이스를 최소 6개로 보강한다.

## 처리한 문제

- `shortest_path-1219`
- `shortest_path-1261`
- `shortest_path-1277`
- `shortest_path-1389`
- `shortest_path-13911`
- `shortest_path-1445`
- `shortest_path-1446`
- `shortest_path-14938`
- `shortest_path-1504`
- `shortest_path-16118`
- `shortest_path-1613`
- `shortest_path-1753`
- `shortest_path-18223`
- `shortest_path-18243`
- `shortest_path-1865`
- `shortest_path-1956`
- `shortest_path-20168`
- `shortest_path-20182`
- `shortest_path-20183`
- `shortest_path-21940`

## 구현 내용

- 이익 그래프에 단일 도시, 유한 이익 경로와 목적지에 영향을 주지 않는 양수 사이클을 추가했다.
- 0-1 BFS와 다익스트라 문제에 빈 벽, 중복 간선, 연결 불가, 우회 경로와 거리 제한 케이스를 추가했다.
- 필수 경유 문제에 경유점 순서가 결과를 바꾸는 입력과 경로가 끊긴 입력을 추가했다.
- 플로이드-워셜 문제에 단방향 관계, 순환 관계, 동률 중심점과 왕복 거리 기준 케이스를 추가했다.
- 벨만-포드 문제에는 시작점에서 닿지 않는 음수 사이클과 연결된 음수 사이클을 모두 추가했다.
- 예산 제한 경로 문제에는 직접 경로와 우회 경로의 최대 간선 비용이 달라지는 입력을 추가했다.

## reference 출력으로 교정한 항목

- `shortest_path-1277`: 연결된 발전소 간선 이후 남은 거리를 반영해 5000으로 교정했다.
- `shortest_path-1445`: 시작점과 도착점 주변의 쓰레기 인접 칸 판정 규칙을 반영했다.
- `shortest_path-1504`: 두 필수 정점을 방문하는 실제 최단 경로 비용을 4로 교정했다.
- `shortest_path-16118`: 늑대의 빠른 첫 이동과 느린 다음 이동을 비교해 여우가 앞서는 정점 수를 1로 교정했다.

## 검증 결과

```text
override self-judge: 20개 모두 AC (각 6/6)
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 85.30
lowQualityCount: 192
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `212 -> 192`로 감소했다.
- 평균 품질 점수가 `84.80 -> 85.30`으로 상승했다.
- 다음 일반 배치는 `shortest_path-2211`부터 진행한다.
