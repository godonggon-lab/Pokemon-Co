# Phase 66 - Low Case Count Hardening Batch 13

## 목표

`case_count_lt_6` 품질 경고가 남아 있던 `dynamic_programming_2-14925`부터
`dynamic_programming_2-1943`까지 20개 override를 보강한다.

완료 기준은 다음과 같다.

- 각 override가 최소 6개의 입력 케이스를 가진다.
- 입력 형식과 문제 제약을 지키는 반례를 추가한다.
- 모든 기대 출력은 문제별 oracle로 생성한다.
- reference solution self-judge가 모든 케이스에서 AC를 받는다.
- 공통 judge 회귀 테스트와 Python 문법 검사가 통과한다.

## 처리한 문제

- `dynamic_programming_2-14925`
- `dynamic_programming_2-14945`
- `dynamic_programming_2-1535`
- `dynamic_programming_2-15724`
- `dynamic_programming_2-1577`
- `dynamic_programming_2-16400`
- `dynamic_programming_2-1695`
- `dynamic_programming_2-17069`
- `dynamic_programming_2-17070`
- `dynamic_programming_2-17208`
- `dynamic_programming_2-17216`
- `dynamic_programming_2-17265`
- `dynamic_programming_2-1727`
- `dynamic_programming_2-17404`
- `dynamic_programming_2-1757`
- `dynamic_programming_2-17845`
- `dynamic_programming_2-1823`
- `dynamic_programming_2-1915`
- `dynamic_programming_2-1937`
- `dynamic_programming_2-1943`

## 구현 내용

- 격자 DP에는 전부 막힌 경우, 가장자리 정답, 내부 장애물과 목적지 차단을 추가했다.
- 누적합과 경로 수 문제에는 단일 행·열, 부분 직사각형, 시작점 인접 차단과 우회 경로를 보강했다.
- 배낭과 자원 선택 문제에는 정확한 한도, 동일 비용, 선택 불가능 및 조합 최적 입력을 추가했다.
- 구간 및 수열 DP에는 전체 팰린드롬, 반복 값, 완전 증가·감소와 양 끝 선택 입력을 추가했다.
- 파이프 이동과 순환 색칠에는 빈 격자, 목적지 장애물, 첫 집과 마지막 집의 색 제약을 드러내는 입력을 추가했다.
- 동전 분할에는 홀수 총합, 정확한 절반 구성, 동전 개수 제한이 결과를 바꾸는 입력을 추가했다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py <batch 13 slugs>
OK: 20 override files self-judged successfully.
각 문제: python AC 6/6
```

```text
python -m unittest harness.tests.test_judge
Ran 9 tests in 2.521s
OK
```

```text
npm.cmd run judge:quality
total: 1009
averageQualityScore: 81.83
lowQualityCount: 332
missingStressCount: 0
allHaveOverride: true
```

```text
python -m py_compile <batch 13 override files>
OK
```

## 작업 결과

- 저품질 override 수가 `352 -> 332`로 20개 감소했다.
- 평균 품질 점수가 `81.33 -> 81.83`으로 상승했다.
- 이번 배치의 20개 override는 모두 최소 6개 케이스와 stress 케이스를 가진다.
- 다음 일반 배치는 `dynamic_programming_2-1958`부터 이어서 처리한다.
