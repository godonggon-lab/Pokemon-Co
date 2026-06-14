# Phase 79 - 저밀도 케이스 보강 배치 26

## 목표

`implementation-1283`부터 `prefix_sum-10427`까지 20개 override의 입력
케이스를 최소 6개로 보강한다.

## 처리한 문제

- `implementation-1283`
- `implementation-16927`
- `implementation-17128`
- `implementation-17276`
- `implementation-17406`
- `implementation-17470`
- `implementation-20327`
- `implementation-21277`
- `implementation-21611`
- `implementation-22858`
- `implementation-22859`
- `implementation-22860`
- `implementation-2469`
- `implementation-5766`
- `implementation-9081`
- `math-22943`
- `math-3343`
- `math-9421`
- `minimum_spanning_tree-1414`
- `prefix_sum-10427`

## 구현 내용

- 단축키 지정에 한 줄 입력, 대소문자 중복, 지정 가능한 문자가 없는 경우를 추가했다.
- 배열 회전에 0회, 한 바퀴, 반복 역연산과 같은 복원 경계를 추가했다.
- 회전 순서가 결과에 영향을 주는 배열 연산과 동일 값 배열을 추가했다.
- HTML 파싱에 단일 문단, 중첩 태그, 연속 공백 정규화 입력을 추가했다.
- 폴더 탐색에 단일 파일, 깊은 폴더, 중복 파일 이름을 추가했다.
- 사다리 복원에 한 줄 사다리와 변경이 필요 없는 경우를 추가했다.
- 다음 순열에 한 글자, 중복 문자, 내림차순 입력을 추가했다.
- 소수 조합과 행복한 소수에 작은 경계값 및 다른 약수 조건을 추가했다.
- 구매 비용 최소화에 한 종류만 사용하는 것이 최적인 입력을 추가했다.
- 랜선 MST에 큰 가중치 연결 그래프와 연결 불가능 그래프를 추가했다.
- 정렬 누적 비용에 원소 1개와 역순 입력을 추가했다.

## 검증 결과

```text
override self-judge: 20개 모두 AC (각 6/6)
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 88.27
lowQualityCount: 72
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `92 -> 72`로 감소했다.
- 평균 품질 점수가 `87.78 -> 88.27`로 상승했다.
- 다음 일반 배치는 `prefix_sum-10713`부터 진행한다.
- 별도 검토가 필요한 2-case override 8개는 일반 배치와 분리해 처리한다.
