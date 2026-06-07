# Phase 42 - Override Expected Output Batch 26

## 목표

Phase 41 이후 남은 override 중 다음 20개 문제의 모든 케이스에 정적 `expected` 출력을 추가한다.

정적 expected를 사용하면 Python과 C++ 등 제출 언어에 관계없이 동일한 입력과 정답으로 채점할 수 있고, 런타임 oracle 의존성을 줄일 수 있다.

## 처리한 문제

1. `greedy-21314`
2. `greedy-2138`
3. `greedy-2141`
4. `greedy-2212`
5. `greedy-2285`
6. `greedy-2457`
7. `greedy-2812`
8. `greedy-2847`
9. `greedy-6068`
10. `greedy-8980`
11. `implementation-1212`
12. `implementation-14719`
13. `implementation-15787`
14. `implementation-15806`
15. `implementation-16935`
16. `implementation-17413`
17. `implementation-21608`
18. `implementation-21918`
19. `implementation-2729`
20. `math-11653`

## 구현 내용

- 기존 edge/stress 입력과 케이스 순서를 유지했다.
- `data/problems*.json`의 Python 정답 코드를 각 입력에 실행해 expected 문자열을 생성했다.
- 미보장 상태였던 총 108개 override 케이스에 expected를 추가했다.
- oracle failure 회귀 테스트의 정상 사용자 코드를 다음 미완료 문제인 `math-1359`로 이동했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 회귀 테스트:

```text
Ran 9 tests in 2.318s
OK
```

전체 override 품질 감사:

```text
total: 1009
averageQualityScore: 71.46
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 잔여 작업

```text
missing_problem: 198
missing_cases: 738
total_cases: 4531
```

다음 배치는 `math-1359`부터 20개씩 처리한다.
