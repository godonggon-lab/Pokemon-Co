# Phase 33 - Override Expected Output Batch 17

## 목표

이전 배치 이후 남아 있던 override 중 다음 20개 문제에 `expected` 출력을 고정한다.

이번 배치의 기준은 다음과 같다.

- 기존 edge/stress 입력은 유지한다.
- 각 override 파일에 `_solve(data: str)`를 추가해 정답 출력을 생성한다.
- Python/C++ 제출 모두 같은 입력과 expected 출력 기준으로 채점될 수 있게 한다.
- expected가 생긴 문제를 oracle failure fixture로 쓰지 않도록 테스트 fixture를 다음 미처리 문제로 이동한다.

## 처리한 문제

1. `dynamic_programming_2-1301`
2. `dynamic_programming_2-13302`
3. `dynamic_programming_2-13398`
4. `dynamic_programming_2-13707`
5. `dynamic_programming_2-13902`
6. `dynamic_programming_2-14226`
7. `dynamic_programming_2-14567`
8. `dynamic_programming_2-14699`
9. `dynamic_programming_2-14728`
10. `dynamic_programming_2-14863`
11. `dynamic_programming_2-14925`
12. `dynamic_programming_2-14945`
13. `dynamic_programming_2-1520`
14. `dynamic_programming_2-1535`
15. `dynamic_programming_2-15724`
16. `dynamic_programming_2-1577`
17. `dynamic_programming_2-16400`
18. `dynamic_programming_2-1695`
19. `dynamic_programming_2-17069`
20. `dynamic_programming_2-17070`

## 구현 메모

- 각 문제의 입력 형식에 맞춰 문자열 기반 `_solve(data: str)`를 작성했다.
- `expected=lambda data: _solve(data)` 형태로 연결해 override의 입력과 출력이 항상 함께 검증되도록 했다.
- `dynamic_programming_2-1301`에 expected가 추가되었기 때문에 `harness/tests/test_judge.py`의 oracle failure 테스트 fixture를 `dynamic_programming_2-17208`로 이동했다.
- 이번 배치는 expected 출력 보강 작업이며, Docker verdict 안정성 문제는 별도 작업으로 분리한다.

## 검증 결과

대상 override 20개를 직접 검증했다.

```text
python scripts/verify-judge-overrides.py \
  dynamic_programming_2-1301 dynamic_programming_2-13302 dynamic_programming_2-13398 \
  dynamic_programming_2-13707 dynamic_programming_2-13902 dynamic_programming_2-14226 \
  dynamic_programming_2-14567 dynamic_programming_2-14699 dynamic_programming_2-14728 \
  dynamic_programming_2-14863 dynamic_programming_2-14925 dynamic_programming_2-14945 \
  dynamic_programming_2-1520 dynamic_programming_2-1535 dynamic_programming_2-15724 \
  dynamic_programming_2-1577 dynamic_programming_2-16400 dynamic_programming_2-1695 \
  dynamic_programming_2-17069 dynamic_programming_2-17070
```

결과:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 테스트:

```text
python -m unittest harness.tests.test_judge
```

결과:

```text
Ran 9 tests in 6.496s
OK
```

품질 점검:

```text
npm run judge:quality
```

결과:

```text
total: 1009
averageQualityScore: 67.89
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 남은 작업

이번 배치 이후 expected 미보강 override는 다음과 같다.

```text
missing_problem 378
missing_cases 1503
total_cases 4531
```

다음 배치는 `dynamic_programming_2-17208`부터 이어서 처리한다.
