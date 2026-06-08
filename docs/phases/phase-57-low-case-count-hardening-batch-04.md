# Phase 57 - Low Case Count Hardening Batch 04

## 목표

낮은 케이스 수(`case_count_lt_6`)로 남아 있던 override 중 `binary_search-1561`부터 `binary_search-20495`까지 20개를 보강했다.

이번 단계의 기준은 다음과 같다.

- 각 override가 최소 6개 이상의 입력 케이스를 가진다.
- 추가 케이스는 문제 제약 안에서 구성한다.
- 출력은 override 내부 `_solve()`로 생성해 언어 중립적인 입력/출력 검증 구조를 유지한다.
- reference solution 기준 self-judge가 모두 AC여야 한다.

## 처리한 문제

- `binary_search-1561`
- `binary_search-15732`
- `binary_search-15810`
- `binary_search-15823`
- `binary_search-16401`
- `binary_search-16434`
- `binary_search-16564`
- `binary_search-16960`
- `binary_search-17124`
- `binary_search-17179`
- `binary_search-17266`
- `binary_search-17393`
- `binary_search-17451`
- `binary_search-17503`
- `binary_search-17951`
- `binary_search-18113`
- `binary_search-18114`
- `binary_search-1939`
- `binary_search-2022`
- `binary_search-20495`

## 구현 내용

- 놀이공원, 도토리 숨기기, 풍선 공장, 민트 초코, 과자 나눠주기 등 이분 탐색 문제의 경계 케이스를 추가했다.
- 단일 원소, 목표값이 작은 경우, 동률 값, 불가능한 결과, 모든 값이 같은 경우, 여러 테스트케이스 입력 등을 섞었다.
- 각 파일은 최소 6개 케이스가 되도록 맞췄다.
- 이미 있던 stress 케이스는 유지하고 edge 케이스를 추가했다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py binary_search-1561 ... binary_search-20495
OK: 20 override files self-judged successfully.
```

```text
python -m unittest harness.tests.test_judge
Ran 9 tests in 14.590s
OK
```

```text
npm.cmd run judge:quality
total: 1009
averageQualityScore: 77.37
lowQualityCount: 511
missingStressCount: 0
allHaveOverride: true
```

```text
python -m py_compile <batch 04 override files>
OK
```

## 남은 작업

- 낮은 품질 카운트는 `533 -> 511`로 감소했다.
- 다음 배치는 `binary_search-20551`부터 이어서 처리한다.
- 이후 목표는 남은 `case_count_lt_6` 문제를 계속 줄이고, 그 다음 fuzz/stress 강도와 TLE/MLE 유도 케이스를 분리해서 강화하는 것이다.
