# Phase 64 - Low Case Count Hardening Batch 11

## 목표

`case_count_lt_6` 품질 경고가 남아 있던 `dynamic_programming_1-1577`부터
`dynamic_programming_1-2491`까지 20개 override를 보강한다.

완료 기준은 다음과 같다.

- 각 override가 최소 6개의 입력 케이스를 가진다.
- 추가 입력이 문제의 입력 제약을 지킨다.
- 기대 출력은 문제별 oracle로 생성한다.
- reference solution self-judge가 모든 케이스에서 AC를 받는다.
- 공통 judge 회귀 테스트와 Python 문법 검사가 통과한다.

## 처리한 문제

- `dynamic_programming_1-1577`
- `dynamic_programming_1-15988`
- `dynamic_programming_1-15991`
- `dynamic_programming_1-15992`
- `dynamic_programming_1-15993`
- `dynamic_programming_1-16194`
- `dynamic_programming_1-16195`
- `dynamic_programming_1-1633`
- `dynamic_programming_1-17175`
- `dynamic_programming_1-17212`
- `dynamic_programming_1-17291`
- `dynamic_programming_1-18353`
- `dynamic_programming_1-1932`
- `dynamic_programming_1-1965`
- `dynamic_programming_1-20152`
- `dynamic_programming_1-20162`
- `dynamic_programming_1-22857`
- `dynamic_programming_1-2293`
- `dynamic_programming_1-2302`
- `dynamic_programming_1-2491`

## 구현 내용

- 경로 DP에는 시작점 인접 도로 차단, 여러 도로 차단, 우회 가능한 구조를 추가했다.
- 합 구성 문제에는 작은 수, 단일 구성, 순서와 사용 횟수 제한이 결과를 바꾸는 입력을 추가했다.
- 카드 구매와 동전 문제에는 최솟값 선택이 단순 탐욕법과 달라지는 조합을 추가했다.
- 수열 문제에는 증가, 감소, 동일 값, 부분 수열 선택이 필요한 입력을 보강했다.
- 상태 선택 문제에는 한쪽 점수가 편향된 입력과 선택 균형이 필요한 입력을 추가했다.
- 기존 stress 케이스는 유지하고 각 override의 전체 케이스 수를 6개로 맞췄다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py <batch 11 slugs>
OK: 20 override files self-judged successfully.
각 문제: python AC 6/6
```

```text
python -m unittest harness.tests.test_judge
Ran 9 tests in 2.497s
OK
```

```text
npm.cmd run judge:quality
total: 1009
averageQualityScore: 80.84
lowQualityCount: 372
missingStressCount: 0
allHaveOverride: true
```

```text
python -m py_compile <batch 11 override files>
OK
```

## 작업 결과

- 저품질 override 수가 `392 -> 372`로 20개 감소했다.
- 이번 배치의 20개 override는 모두 최소 6개 케이스와 stress 케이스를 가진다.
- 다음 일반 배치는 `dynamic_programming_1-2565`부터 이어서 처리한다.
- 품질 목록 상단의 일부 2케이스 override는 별도 우선순위 그룹으로 추적한다.
