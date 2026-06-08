# Phase 60 - Low Case Count Hardening Batch 07

## 목표

낮은 케이스 수(`case_count_lt_6`)로 남아 있던 override 중 `brute_force-1548`부터 `brute_force-18868`까지 20개를 보강했다.

이번 단계의 기준은 다음과 같다.

- 각 override가 최소 6개 이상의 입력 케이스를 가진다.
- 추가 케이스는 문제 제약 안에서 구성한다.
- 출력은 override 내부 `_solve()`로 생성해 언어 중립적인 입력/출력 검증 구조를 유지한다.
- reference solution 기준 self-judge가 모두 AC여야 한다.

## 처리한 문제

- `brute_force-1548`
- `brute_force-15686`
- `brute_force-15728`
- `brute_force-15779`
- `brute_force-1581`
- `brute_force-15970`
- `brute_force-16508`
- `brute_force-16637`
- `brute_force-1668`
- `brute_force-16937`
- `brute_force-16943`
- `brute_force-16951`
- `brute_force-16986`
- `brute_force-17085`
- `brute_force-1711`
- `brute_force-17484`
- `brute_force-17521`
- `brute_force-17610`
- `brute_force-18512`
- `brute_force-18868`

## 구현 내용

- 완전탐색 문제에 최소 입력, 불가능 입력, 반복 값, 동률, 작은 격자, 단조 수열 케이스를 추가했다.
- 순열/조합/격자 탐색이 포함된 문제는 검증 시간이 튀지 않도록 작은 입력 위주로 보강했다.
- 기존 stress 케이스는 유지하고 edge 케이스를 추가해 최소 6개 케이스를 맞췄다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py brute_force-1548 ... brute_force-18868
OK: 20 override files self-judged successfully.
```

```text
python -m unittest harness.tests.test_judge
Ran 9 tests in 10.976s
OK
```

```text
npm.cmd run judge:quality
total: 1009
averageQualityScore: 78.86
lowQualityCount: 451
missingStressCount: 0
allHaveOverride: true
```

```text
python -m py_compile <batch 07 override files>
OK
```

## 남은 작업

- 낮은 품질 카운트는 `471 -> 451`로 감소했다.
- 다음 배치는 `brute_force-19947`부터 이어서 처리한다.
- 낮은 케이스 수 보강을 계속 진행한 뒤, fuzz/stress 강도와 TLE/MLE 유도 케이스를 별도 단계로 강화한다.
