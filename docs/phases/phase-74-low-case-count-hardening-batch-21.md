# Phase 74 - 저빈도 케이스 보강 배치 21

## 목표

`shortest_path-2211`부터 `simulation-16939`까지
20개 override의 입력 케이스를 최소 6개로 보강한다.

## 처리한 문제

- `shortest_path-2211`
- `shortest_path-2224`
- `shortest_path-22865`
- `shortest_path-22870`
- `shortest_path-2307`
- `shortest_path-2458`
- `shortest_path-2660`
- `shortest_path-2982`
- `shortest_path-4485`
- `shortest_path-5972`
- `shortest_path-9205`
- `simulation-13459`
- `simulation-13460`
- `simulation-14594`
- `simulation-15644`
- `simulation-15653`
- `simulation-15683`
- `simulation-15685`
- `simulation-16235`
- `simulation-16939`

## 구현 내용

- 최단 경로 트리 문제에 단일 간선, 중복 간선과 우회 경로를 추가했다.
- 관계 추론 문제에 자기 명제, 순환 명제, 대소문자가 섞인 전이 관계를 추가했다.
- 다중 시작점 최단 경로에 동률 후보와 일렬 그래프를 추가했다.
- 왕복 산책 문제에는 사전순 최단 경로와 복귀 경로가 달라지는 입력을 추가했다.
- 간선 제거 지연 문제에는 대체 경로가 없는 경우와 동일 비용 대체 경로를 추가했다.
- 시뮬레이션 문제에는 즉시 성공, 단일 CCTV, 빈 나무 칸, 짧은 드래곤 커브와 완성 상태 큐브를 추가했다.
- 구슬 탈출 4는 custom checker로 이동 횟수와 실제 이동 문자열을 함께 검증했다.

## reference 출력으로 교정한 항목

- `shortest_path-22865`: 세 친구까지의 최소 거리 기준으로 가장 먼 정점을 2로 교정했다.
- `shortest_path-22870`: 직접 최단 경로를 제거한 뒤 복귀하는 삼각형 입력의 합을 2로 교정했다.
- `shortest_path-2982`: 왕의 이동 시간이 끝난 뒤 통과 가능한 최단 시간을 6으로 교정했다.
- 구슬 탈출 문제의 세로 통로 입력은 한 번의 아래 이동으로 성공하는 결과를 반영했다.
- `simulation-15685`: 짧은 2세대 드래곤 커브가 단위 정사각형을 만들지 않는 결과를 반영했다.

## 검증 결과

```text
override self-judge: 20개 모두 AC (각 6/6)
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 85.79
lowQualityCount: 172
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `192 -> 172`로 감소했다.
- 평균 품질 점수가 `85.30 -> 85.79`로 상승했다.
- 다음 일반 배치는 `simulation-17135`부터 진행한다.
