# Phase 76 - 저빈도 케이스 보강 배치 23

## 목표

`simulation-8972`부터 `tree-1595`까지
20개 override의 입력 케이스를 최소 6개로 보강한다.

## 처리한 문제

- `simulation-8972`
- `string-1942`
- `string-2922`
- `topological_sorting-14676`
- `topological_sorting-1948`
- `topological_sorting-20119`
- `topological_sorting-21276`
- `topological_sorting-2252`
- `topological_sorting-2623`
- `topological_sorting-3665`
- `topological_sorting-9470`
- `tree-1167`
- `tree-1240`
- `tree-12896`
- `tree-12912`
- `tree-14267`
- `tree-14570`
- `tree-14657`
- `tree-15900`
- `tree-1595`

## 구현 내용

- 미친 아두이노 문제에 즉시 충돌, 이동 후 생존과 로봇끼리 충돌하는 입력을 추가했다.
- 시간 문자열 문제에 자정 경계, 단일 초 구간과 하루를 거꾸로 순환하는 구간을 추가했다.
- 즐거운 단어 문제에 `L` 부재, 연속 빈칸과 고정된 `L`이 있는 조합을 추가했다.
- 건물 게임 문제에 중복 건설, 선행 건물 미건설과 철거 오류를 추가했다.
- 위상 정렬 문제에 단일 정점, 독립 정점, 일자 DAG, 사이클과 순위 역전을 추가했다.
- 트리 문제에 단일 노드, 별 모양, 일자 모양, 동일 노드 거리와 깊은 경로를 추가했다.
- 복수 정답이 허용되는 위상 정렬 문제는 기존 custom checker로 제약 만족 여부를 검증했다.

## reference 출력으로 교정한 항목

- `string-2922`: 세 개 빈칸과 `L_A`의 실제 가능한 문자열 수를 각각 690, 26으로 교정했다.
- `topological_sorting-20119`: 재료가 모두 있어야 완성되는 제조법 조건을 반영했다.
- `topological_sorting-3665`: 두 순위 뒤집기로 사이클이 생기는 입력을 `IMPOSSIBLE`로 교정했다.
- `tree-14657`: 이동 거리 제한 내에서 선택되는 노드 계산 결과를 교정했다.
- `tree-15900`: 깊이 3의 단일 리프를 가진 일자 트리의 홀수 깊이 합을 `Yes`로 교정했다.

## 검증 결과

```text
override self-judge: 20개 모두 AC (각 6/6)
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 86.78
lowQualityCount: 132
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `152 -> 132`로 감소했다.
- 평균 품질 점수가 `86.29 -> 86.78`로 상승했다.
- 다음 일반 배치는 `tree-16437`부터 진행한다.
