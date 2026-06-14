# Phase 78 - 저밀도 케이스 보강 배치 25

## 목표

`trie-9202`부터 `implementation-10703`까지 20개 override의 입력 케이스를
최소 6개로 보강한다.

## 처리한 문제

- `trie-9202`
- `two_pointer-10025`
- `two_pointer-15831`
- `two_pointer-16472`
- `two_pointer-20366`
- `two_pointer-20442`
- `two_pointer-2118`
- `two_pointer-21279`
- `two_pointer-21921`
- `two_pointer-22862`
- `two_pointer-2428`
- `two_pointer-6137`
- `graph_traversal-14248`
- `graph_traversal-18232`
- `graph_traversal-3184`
- `graph_traversal-3187`
- `graph_traversal-5567`
- `greedy-18234`
- `implementation-1022`
- `implementation-10703`

## 구현 내용

- 보글 문제에 한 글자 단어, 같은 단어를 여러 경로로 찾는 경우, 최장 단어 동률을 추가했다.
- 투 포인터 문제에 창 크기 1, 답이 0인 경우, 모든 원소가 포함되는 경우와 동률 구간을 추가했다.
- 원형 거리, 눈사람 쌍, 파일 크기 비교에 같은 값과 양 끝 경계 입력을 추가했다.
- 최장 짝수 부분수열과 흑백 문자열에 삭제 가능 개수 0, 정확히 한도만큼 삭제하는 경우를 추가했다.
- 점프와 텔레포트 탐색에 시작점과 도착점이 같은 경우, 전 노드 연결, 지름길 연쇄를 추가했다.
- 양과 늑대 영역 탐색에 열린 영역과 벽으로 닫힌 영역의 우세 조건을 추가했다.
- 결혼식 그래프에 직접 친구와 정확히 두 단계인 친구를 구분하는 입력을 추가했다.
- 소용돌이 좌표 출력과 유성 낙하에 단일 행, 비대칭 좌표, 최소·최대 낙하 거리를 추가했다.

## reference 검증 중 교정한 항목

- `graph_traversal-14248`: 시작점에서 양방향 점프를 반복하면 모든 돌에 도달하는 입력의 기대값을 교정했다.
- `two_pointer-21279`: 선택 가능한 직사각형의 축 제한과 최대 광물 합을 reference 결과에 맞춰 교정했다.
- `two_pointer-22862`: 홀수 2개를 제거한 뒤 남는 연속 짝수 개수를 3으로 교정했다.

## 검증 결과

```text
override self-judge: 20개 모두 AC (각 6/6)
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 87.78
lowQualityCount: 92
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `112 -> 92`로 감소했다.
- 평균 품질 점수가 `87.28 -> 87.78`로 상승했다.
- 다음 일반 배치는 `implementation-1283`부터 진행한다.
- 별도 검토가 필요한 2-case override 8개는 일반 배치와 분리해 처리한다.
