# Phase 34 - Override Expected Output Batch 18

## 목표

Phase 33 이후 남아 있던 override 중 다음 20개 문제에 `expected` 출력을 고정한다.

현재 작업은 단순히 judge case를 새로 늘리는 단계가 아니라, 이미 준비된 edge/stress 입력 케이스가 실제 채점에서 바로 쓰일 수 있도록 정답 출력을 붙이는 단계다. 이렇게 해야 Python/C++ 제출 모두 같은 입력과 같은 expected 출력 기준으로 안정적으로 판정된다.

## 처리한 문제

1. `dynamic_programming_2-17208`
2. `dynamic_programming_2-17216`
3. `dynamic_programming_2-17265`
4. `dynamic_programming_2-1727`
5. `dynamic_programming_2-17404`
6. `dynamic_programming_2-17485`
7. `dynamic_programming_2-1757`
8. `dynamic_programming_2-17845`
9. `dynamic_programming_2-1823`
10. `dynamic_programming_2-18427`
11. `dynamic_programming_2-1915`
12. `dynamic_programming_2-1937`
13. `dynamic_programming_2-1943`
14. `dynamic_programming_2-1958`
15. `dynamic_programming_2-19645`
16. `dynamic_programming_2-20181`
17. `dynamic_programming_2-20542`
18. `dynamic_programming_2-2056`
19. `dynamic_programming_2-20667`
20. `dynamic_programming_2-2073`

## 구현 메모

- 각 override 파일에 `_solve(data: str)`를 추가했다.
- 기존 `edge`, `stress` 입력은 유지하고 `_with_expected`로 expected를 채웠다.
- `dynamic_programming_2-17208`에 expected가 추가되었기 때문에 oracle failure 테스트 fixture는 다음 미보강 문제인 `dynamic_programming_2-2157`로 이동했다.
- 이번 배치는 입력 케이스 수를 늘리는 작업이 아니라, 기존 입력 케이스를 정답 출력까지 포함한 완성형 judge case로 바꾸는 작업이다.

## 검증 결과

대상 override 20개 직접 검증:

```text
python scripts/verify-judge-overrides.py \
  dynamic_programming_2-17208 dynamic_programming_2-17216 dynamic_programming_2-17265 \
  dynamic_programming_2-1727 dynamic_programming_2-17404 dynamic_programming_2-17485 \
  dynamic_programming_2-1757 dynamic_programming_2-17845 dynamic_programming_2-1823 \
  dynamic_programming_2-18427 dynamic_programming_2-1915 dynamic_programming_2-1937 \
  dynamic_programming_2-1943 dynamic_programming_2-1958 dynamic_programming_2-19645 \
  dynamic_programming_2-20181 dynamic_programming_2-20542 dynamic_programming_2-2056 \
  dynamic_programming_2-20667 dynamic_programming_2-2073
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
Ran 9 tests in 2.979s
OK
```

품질 점검:

```text
npm run judge:quality
```

결과:

```text
total: 1009
averageQualityScore: 68.29
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 남은 작업

이번 배치 이후 expected 미보강 override는 다음과 같다.

```text
missing_problem 358
missing_cases 1435
total_cases 4531
```

다음 배치는 `dynamic_programming_2-2157`부터 이어서 처리한다.
