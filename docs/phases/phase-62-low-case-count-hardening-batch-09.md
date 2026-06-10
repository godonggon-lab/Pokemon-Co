# Phase 62 - Low Case Count Hardening Batch 09

## 목표

낮은 케이스 수(`case_count_lt_6`)로 남아 있던 실제 품질 대상 중 `data_structure2-9375`부터 `divide_and_conquer-2374`까지 20개를 보강했다.

이번 단계의 기준은 다음과 같다.

- 각 override가 최소 6개 이상의 입력 케이스를 가진다.
- 추가 케이스는 문제 제약 안에서 구성한다.
- 일반 출력은 override 내부 `_solve()`로 생성한다.
- 정답 형태가 여러 개인 문제는 기존 `check_output()` 검증을 유지한다.
- reference solution 기준 self-judge가 모두 AC여야 한다.

## 처리한 문제

- `data_structure2-9375`
- `disjoint_set-11085`
- `disjoint_set-12893`
- `disjoint_set-14595`
- `disjoint_set-15789`
- `disjoint_set-16168`
- `disjoint_set-16724`
- `disjoint_set-17090`
- `disjoint_set-17398`
- `disjoint_set-20040`
- `disjoint_set-20955`
- `disjoint_set-3108`
- `disjoint_set-7511`
- `divide_and_conquer-1030`
- `divide_and_conquer-14600`
- `divide_and_conquer-14601`
- `divide_and_conquer-1493`
- `divide_and_conquer-16438`
- `divide_and_conquer-1780`
- `divide_and_conquer-2374`

## 구현 내용

- 분리 집합 문제에 단일 컴포넌트, 분리 그래프, 사이클, 중복 연결, 역순 간선 복원 케이스를 추가했다.
- 방향 격자 문제에는 탈출 경로와 순환 경로를 나누어 보강했다.
- 분할 정복 문제에는 최소 크기, 균일 영역, 혼합 영역, 구간 출력 및 큐브 부족 케이스를 추가했다.
- 트로미노와 문자 분류 문제는 여러 정답이 가능하므로 기존 특수 checker를 그대로 사용했다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py data_structure2-9375 ... divide_and_conquer-2374
OK: 20 override files self-judged successfully.
```

```text
python -m unittest harness.tests.test_judge
Ran 9 tests in 2.404s
OK
```

```text
npm.cmd run judge:quality
total: 1009
averageQualityScore: 79.85
lowQualityCount: 411
missingStressCount: 0
allHaveOverride: true
```

```text
python -m py_compile <batch 09 override files>
OK
```

## 남은 작업

- 품질 감사의 낮은 품질 카운트는 `431 -> 411`로 감소했다.
- 다음 배치는 `dynamic_programming_1-10211`부터 이어서 처리한다.
- 낮은 케이스 수 보강 이후 fuzz/stress 강도와 TLE/MLE 유도 케이스를 별도 단계로 강화한다.
