# Phase 67 - Low Case Count Hardening Batch 14

## 목표

`dynamic_programming_2-1958`부터 `dynamic_programming_2-2688`까지
20개 override의 입력 케이스를 최소 6개로 보강한다.

## 처리한 문제

- `dynamic_programming_2-1958`
- `dynamic_programming_2-19645`
- `dynamic_programming_2-20002`
- `dynamic_programming_2-20181`
- `dynamic_programming_2-20542`
- `dynamic_programming_2-2056`
- `dynamic_programming_2-20667`
- `dynamic_programming_2-2073`
- `dynamic_programming_2-2157`
- `dynamic_programming_2-21925`
- `dynamic_programming_2-21941`
- `dynamic_programming_2-2228`
- `dynamic_programming_2-2229`
- `dynamic_programming_2-2253`
- `dynamic_programming_2-2411`
- `dynamic_programming_2-2616`
- `dynamic_programming_2-2624`
- `dynamic_programming_2-2629`
- `dynamic_programming_2-2631`
- `dynamic_programming_2-2688`

## 구현 내용

- LCS와 문자열 DP에 완전 일치, 불일치, 반복 문자와 부분 공통 수열을 추가했다.
- 제한 배낭과 자원 선택에는 정확한 한도, 불가능 상태, 동일 비용 조합을 보강했다.
- DAG 일정과 경로 문제에는 독립 작업, 긴 의존 체인, 역방향 간선 무시 케이스를 추가했다.
- 구간 선택과 수열 DP에는 전체 음수, 분리 구간, 증가·감소·동일 값 입력을 추가했다.
- 동전, 추, 소형 기관차 문제에는 개수 제한과 정확한 합이 결과를 바꾸는 입력을 보강했다.
- 격자 경로에는 아이템 순서, 장애물 차단, 아이템 없는 기본 경로를 추가했다.

## 검증 결과

```text
override self-judge: 20개 모두 python AC 6/6
unittest: 9 tests OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 82.32
lowQualityCount: 312
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `332 -> 312`로 감소했다.
- 평균 품질 점수가 `81.83 -> 82.32`로 상승했다.
- 다음 일반 배치는 `dynamic_programming_2-2758`부터 진행한다.
