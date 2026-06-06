# Phase 41 - Override Expected Output Batch 25

## 목표

Phase 40 이후 남은 override 중 다음 20개 문제의 모든 케이스에 정적 `expected` 출력을 추가한다.

정적 expected는 사용자 코드 언어와 관계없이 같은 입력과 정답을 사용하게 하며, 채점마다 Python oracle을 다시 실행하면서 발생할 수 있는 실패를 줄인다.

## 처리한 문제

1. `greedy-1474`
2. `greedy-14916`
3. `greedy-16162`
4. `greedy-16206`
5. `greedy-16208`
6. `greedy-16435`
7. `greedy-1715`
8. `greedy-1744`
9. `greedy-1758`
10. `greedy-17615`
11. `greedy-1817`
12. `greedy-1931`
13. `greedy-1946`
14. `greedy-19539`
15. `greedy-19598`
16. `greedy-19939`
17. `greedy-20115`
18. `greedy-20117`
19. `greedy-2109`
20. `greedy-21313`

## 구현 내용

- 기존 edge/stress 입력과 케이스 순서를 유지했다.
- `data/problems*.json`의 Python 정답 코드를 각 입력에 실행해 expected 문자열을 생성했다.
- 총 106개 override 케이스를 정적 expected 기반으로 검증했다.
- 미보장 케이스 106개를 모두 보완했다.
- oracle failure 회귀 테스트의 정상 사용자 코드를 다음 미완료 문제인 `greedy-21314`로 이동했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 회귀 테스트:

```text
Ran 9 tests in 2.337s
OK
```

전체 override 품질 감사:

```text
total: 1009
averageQualityScore: 71.07
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 잔여 작업

```text
missing_problem: 218
missing_cases: 846
total_cases: 4531
```

다음 배치는 `greedy-21314`부터 20개씩 처리한다.
