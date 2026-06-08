# Phase 58 - Low Case Count Hardening Batch 05

## 목표

낮은 케이스 수(`case_count_lt_6`)로 남아 있던 override 중 `binary_search-20551`부터 `brute_force-10448`까지 20개를 보강했다.

이번 단계의 기준은 다음과 같다.

- 각 override가 최소 6개 이상의 입력 케이스를 가진다.
- 추가 케이스는 문제 제약 안에서 구성한다.
- 출력은 override 내부 `_solve()` 또는 기존 `_solve(stdin)` 호출로 생성해 언어 중립적인 입력/출력 검증 구조를 유지한다.
- reference solution 기준 self-judge가 모두 AC여야 한다.

## 처리한 문제

- `binary_search-20551`
- `binary_search-2121`
- `binary_search-22871`
- `binary_search-22945`
- `binary_search-2343`
- `binary_search-2412`
- `binary_search-2467`
- `binary_search-2613`
- `binary_search-2792`
- `binary_search-2866`
- `binary_search-3020`
- `binary_search-6209`
- `binary_search-7453`
- `binary_search-7795`
- `binary_search-8983`
- `binary_search-9007`
- `brute_force-1018`
- `brute_force-1025`
- `brute_force-1034`
- `brute_force-10448`

## 구현 내용

- 이분 탐색 문제에는 중복 값, 단일 값, 전체 제거/미제거, 동률, 불가능 판정, 여러 테스트케이스 입력을 섞었다.
- brute force 문제에는 최소 보드, 반복 패턴, 완전 일치/불일치, 큰 수 후보, 여러 질의 입력을 추가했다.
- 기존 stress 케이스는 유지하고 edge 케이스를 추가해 최소 6개 케이스를 맞췄다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py binary_search-20551 ... brute_force-10448
OK: 20 override files self-judged successfully.
```

```text
python -m unittest harness.tests.test_judge
Ran 9 tests in 6.586s
OK
```

```text
npm.cmd run judge:quality
total: 1009
averageQualityScore: 77.86
lowQualityCount: 491
missingStressCount: 0
allHaveOverride: true
```

```text
python -m py_compile <batch 05 override files>
OK
```

## 남은 작업

- 낮은 품질 카운트는 `511 -> 491`로 감소했다.
- 다음 배치는 `brute_force-10472`부터 이어서 처리한다.
- 낮은 케이스 수를 먼저 줄인 뒤, fuzz/stress 강도와 TLE/MLE 유도 케이스를 별도 축으로 강화한다.
