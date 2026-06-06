# Phase 40 - Override Expected Output Batch 24

## 목표

Phase 39 이후 남은 override 중 다음 20개 문제의 모든 케이스에 정적 `expected` 출력을 추가한다.

정적 expected가 있으면 사용자 코드 채점 시 Python oracle을 매번 실행하지 않아도 되므로, 언어와 무관하게 동일한 입력과 정답으로 Python/C++ 제출을 검증할 수 있다.

## 처리한 문제

1. `graph_traversal-9019`
2. `graph_traversal-9466`
3. `greedy-1080`
4. `greedy-11000`
5. `greedy-11047`
6. `greedy-11399`
7. `greedy-11508`
8. `greedy-11509`
9. `greedy-12782`
10. `greedy-13019`
11. `greedy-13164`
12. `greedy-13413`
13. `greedy-1343`
14. `greedy-1374`
15. `greedy-13975`
16. `greedy-14247`
17. `greedy-1439`
18. `greedy-14400`
19. `greedy-1449`
20. `greedy-1455`

## 구현 내용

- 기존 edge/stress 입력은 유지했다.
- `data/problems*.json`에 저장된 Python 정답 코드를 각 입력에 실행해 expected 문자열을 생성했다.
- 총 110개 케이스를 정적 expected 기반으로 검증했다.
- 이번 배치에서 expected가 없던 105개 케이스를 보완했다.
- oracle failure 회귀 테스트의 정상 사용자 코드를 다음 미완료 문제인 `greedy-1474`로 이동했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 회귀 테스트:

```text
Ran 9 tests in 2.256s
OK
```

전체 override 품질 감사:

```text
total: 1009
averageQualityScore: 70.67
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 잔여 작업

```text
missing_problem: 238
missing_cases: 952
total_cases: 4531
```

다음 배치는 `greedy-1474`부터 20개씩 처리한다.
