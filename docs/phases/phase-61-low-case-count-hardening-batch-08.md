# Phase 61 - Low Case Count Hardening Batch 08

## 목표

낮은 케이스 수(`case_count_lt_6`)로 남아 있던 실제 품질 대상 중 `brute_force-1895`부터 `data_structure2-21944`까지 20개를 보강했다.

이번 단계의 기준은 다음과 같다.

- 각 일반 override가 최소 6개 이상의 입력 케이스를 가진다.
- 추가 케이스는 문제 제약 안에서 구성한다.
- 출력은 override 내부 `_solve()`로 생성해 언어 중립적인 입력/출력 구조를 유지한다.
- reference solution 기준 self-judge가 모두 AC여야 한다.

## 처리한 문제

- `brute_force-1895`
- `brute_force-19947`
- `brute_force-2160`
- `brute_force-21943`
- `brute_force-2304`
- `brute_force-2435`
- `brute_force-2635`
- `brute_force-2961`
- `brute_force-3040`
- `brute_force-3085`
- `brute_force-5671`
- `brute_force-5883`
- `brute_force-9996`
- `data_structure-1863`
- `data_structure-22866`
- `data_structure2-12764`
- `data_structure2-1655`
- `data_structure2-17255`
- `data_structure2-19583`
- `data_structure2-21944`

## 품질 예외 처리

`brute_force-4690`은 입력 없이 정해진 전체 출력을 생성하는 문제다. 동일한 빈 입력 케이스를 복제하는 것은 검증력을 높이지 않으므로 기존 `QUALITY_EXCEPTION`과 단일 exhaustive stress 케이스를 유지했다.

## 구현 내용

- 영상 필터, 연속 투자, 그림 비교, 수열 및 부분집합 문제에 최소값과 반복값 경계를 추가했다.
- 문자열 패턴, 스카이라인, 중앙값, 좌석 배정 및 추천 시스템에 동률과 추가/삭제 흐름을 보강했다.
- 기존 stress 케이스는 유지하고 edge 케이스를 추가해 일반 override를 최소 6개 케이스로 맞췄다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py brute_force-1895 ... data_structure2-21944
OK: 20 override files self-judged successfully.
```

```text
python -m unittest harness.tests.test_judge
Ran 9 tests in 6.859s
OK
```

```text
npm.cmd run judge:quality
total: 1009
averageQualityScore: 79.35
lowQualityCount: 431
missingStressCount: 0
allHaveOverride: true
```

```text
python -m py_compile <batch 08 override files>
OK
```

## 남은 작업

- 품질 감사의 낮은 품질 카운트는 `451 -> 431`로 감소했다.
- 다음 배치는 `data_structure2-9375`부터 이어서 처리한다.
- 낮은 케이스 수 보강 이후 fuzz/stress 강도와 TLE/MLE 유도 케이스를 별도 단계로 강화한다.
