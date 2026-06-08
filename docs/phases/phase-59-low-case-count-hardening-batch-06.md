# Phase 59 - Low Case Count Hardening Batch 06

## 목표

낮은 케이스 수(`case_count_lt_6`)로 남아 있던 override 중 `brute_force-10472`부터 `brute_force-1543`까지 20개를 보강했다.

이번 단계의 기준은 다음과 같다.

- 각 override가 최소 6개 이상의 입력 케이스를 가진다.
- 추가 케이스는 문제 제약 안에서 구성한다.
- 출력은 override 내부 `_solve()`로 생성해 언어 중립적인 입력/출력 검증 구조를 유지한다.
- reference solution 기준 self-judge가 모두 AC여야 한다.

## 처리한 문제

- `brute_force-10472`
- `brute_force-1059`
- `brute_force-11170`
- `brute_force-1120`
- `brute_force-11502`
- `brute_force-1251`
- `brute_force-1254`
- `brute_force-12919`
- `brute_force-1359`
- `brute_force-1411`
- `brute_force-1421`
- `brute_force-14225`
- `brute_force-14391`
- `brute_force-14501`
- `brute_force-1487`
- `brute_force-14912`
- `brute_force-1503`
- `brute_force-1527`
- `brute_force-15270`
- `brute_force-1543`

## 구현 내용

- 완전탐색 문제의 최소 입력, 반복 패턴, 불가능 케이스, 경계 숫자, 다중 테스트케이스 입력을 추가했다.
- 비트마스크 완전탐색 문제(`brute_force-14391`)는 검증 시간이 튀지 않도록 작은 보드 위주로 보강했다.
- 기존 stress 케이스는 유지하고 edge 케이스를 추가해 최소 6개 케이스를 맞췄다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py brute_force-10472 ... brute_force-1543
OK: 20 override files self-judged successfully.
```

```text
python -m unittest harness.tests.test_judge
Ran 9 tests in 10.972s
OK
```

```text
npm.cmd run judge:quality
total: 1009
averageQualityScore: 78.36
lowQualityCount: 471
missingStressCount: 0
allHaveOverride: true
```

```text
python -m py_compile <batch 06 override files>
OK
```

## 남은 작업

- 낮은 품질 카운트는 `491 -> 471`로 감소했다.
- 다음 배치는 `brute_force-15686`부터 이어서 처리한다.
- 낮은 케이스 수 보강을 계속 진행한 뒤, fuzz/stress 강도와 TLE/MLE 유도 케이스를 별도 단계로 강화한다.
