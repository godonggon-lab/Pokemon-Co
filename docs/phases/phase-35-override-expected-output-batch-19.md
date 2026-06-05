# Phase 35 - Override Expected Output Batch 19

## 목표

Phase 34 이후 남아 있던 override 중 다음 20개 문제에 `expected` 출력을 고정한다.

이 작업은 judge case를 무작정 추가하는 것이 아니라, 이미 존재하는 edge/stress 입력을 실제 채점 가능한 완성형 케이스로 바꾸는 단계다. expected가 들어가면 사용자 제출과 oracle 제출을 매번 비교하지 않아도 Python/C++ 제출을 같은 입력과 같은 정답 출력 기준으로 판정할 수 있다.

## 처리한 문제

1. `dynamic_programming_2-2157`
2. `dynamic_programming_2-21923`
3. `dynamic_programming_2-21925`
4. `dynamic_programming_2-21941`
5. `dynamic_programming_2-2225`
6. `dynamic_programming_2-2228`
7. `dynamic_programming_2-2229`
8. `dynamic_programming_2-2253`
9. `dynamic_programming_2-2411`
10. `dynamic_programming_2-2616`
11. `dynamic_programming_2-2624`
12. `dynamic_programming_2-2629`
13. `dynamic_programming_2-2631`
14. `dynamic_programming_2-2688`
15. `dynamic_programming_2-2758`
16. `dynamic_programming_2-3067`
17. `dynamic_programming_2-4095`
18. `dynamic_programming_2-4811`
19. `dynamic_programming_2-5557`
20. `dynamic_programming_2-5569`

## 구현 메모

- 각 override 파일에 `_solve(data: str)`를 추가했다.
- 기존 `edge`, `stress` 입력은 유지하고 `_with_expected`로 expected를 채웠다.
- `dynamic_programming_2-2157`에 expected가 추가되었기 때문에 oracle failure 테스트 fixture는 다음 미보강 문제인 `dynamic_programming_2-5582`로 이동했다.
- `dynamic_programming_2-21923`, `dynamic_programming_2-5557`처럼 기존 샘플보다 케이스 수가 많은 문제도 모든 케이스가 expected를 갖도록 보강했다.

## 검증 결과

대상 override 20개 직접 검증:

```text
python scripts/verify-judge-overrides.py \
  dynamic_programming_2-2157 dynamic_programming_2-21923 dynamic_programming_2-21925 \
  dynamic_programming_2-21941 dynamic_programming_2-2225 dynamic_programming_2-2228 \
  dynamic_programming_2-2229 dynamic_programming_2-2253 dynamic_programming_2-2411 \
  dynamic_programming_2-2616 dynamic_programming_2-2624 dynamic_programming_2-2629 \
  dynamic_programming_2-2631 dynamic_programming_2-2688 dynamic_programming_2-2758 \
  dynamic_programming_2-3067 dynamic_programming_2-4095 dynamic_programming_2-4811 \
  dynamic_programming_2-5557 dynamic_programming_2-5569
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
Ran 9 tests in 18.787s
OK
```

품질 점검:

```text
npm run judge:quality
```

결과:

```text
total: 1009
averageQualityScore: 68.69
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 남은 작업

이번 배치 이후 expected 미보강 override는 다음과 같다.

```text
missing_problem 338
missing_cases 1366
total_cases 4531
```

다음 배치는 `dynamic_programming_2-5582`부터 이어서 처리한다.
