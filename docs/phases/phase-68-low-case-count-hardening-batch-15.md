# Phase 68 - Low Case Count Hardening Batch 15

## 목표

`dynamic_programming_2-2758`부터 `graph_traversal-13913`까지
20개 override의 입력 케이스를 최소 6개로 보강한다.

## 처리한 문제

- `dynamic_programming_2-2758`
- `dynamic_programming_2-3067`
- `dynamic_programming_2-4095`
- `dynamic_programming_2-4811`
- `dynamic_programming_2-5569`
- `dynamic_programming_2-5582`
- `dynamic_programming_2-5624`
- `dynamic_programming_2-9084`
- `dynamic_programming_on_trees-12978`
- `dynamic_programming_on_trees-2058`
- `graph_traversal-10026`
- `graph_traversal-10711`
- `graph_traversal-11123`
- `graph_traversal-11559`
- `graph_traversal-1240`
- `graph_traversal-12761`
- `graph_traversal-12851`
- `graph_traversal-1303`
- `graph_traversal-13565`
- `graph_traversal-13913`

## 구현 내용

- 조합 및 동전 DP에는 최소 목표, 구성 불가능, 여러 테스트케이스 입력을 추가했다.
- 최대 정사각형과 경로 DP에는 전부 0인 격자, 직사각형, 다중 데이터 입력을 보강했다.
- 문자열 DP에는 완전 일치, 완전 불일치, 긴 공통 부분 문자열을 추가했다.
- 트리 DP에는 단일 정점, 별 모양, 긴 경로와 가중 독립 집합 입력을 추가했다.
- 그래프 탐색에는 단일 컴포넌트, 대각선 분리, 도달 불가, 시작점과 목적지가 같은 입력을 보강했다.
- 고정 기대값을 사용하는 override는 reference solution의 동작을 확인한 뒤 결과를 기록했다.

## 검증 중 발견한 사항

`dynamic_programming_2-5569`에 처음 추가한 단일 행·열 입력은 문제의 실제 제약인
가로와 세로 2 이상을 위반했다. 해당 입력과 임시 oracle 분기를 제거하고,
`2x3`, `3x2`, `3x3` 유효 경계 입력으로 교체했다.

## 검증 결과

```text
override self-judge: 20개 모두 python AC 6/6
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 82.82
lowQualityCount: 292
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `312 -> 292`로 감소했다.
- 평균 품질 점수가 `82.32 -> 82.82`로 상승했다.
- 다음 일반 배치는 `graph_traversal-14442`부터 진행한다.
