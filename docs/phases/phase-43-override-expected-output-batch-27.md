# Phase 43 - Override Expected Output Batch 27

## 목표

Phase 42 이후 남은 override 중 다음 20개 문제의 모든 케이스에 정적 `expected` 출력을 추가한다.

정적 expected를 사용해 제출 언어와 무관한 입력/정답 계약을 만들고, 실제 채점 중 Python oracle 실행에 의존하는 범위를 줄인다.

## 처리한 문제

1. `math-1359`
2. `math-1978`
3. `math-21312`
4. `math-21919`
5. `math-21920`
6. `math-2753`
7. `math-5618`
8. `minimum_spanning_tree-10423`
9. `minimum_spanning_tree-1045`
10. `minimum_spanning_tree-13418`
11. `minimum_spanning_tree-1368`
12. `minimum_spanning_tree-13905`
13. `minimum_spanning_tree-1414`
14. `minimum_spanning_tree-14950`
15. `minimum_spanning_tree-16202`
16. `minimum_spanning_tree-17472`
17. `minimum_spanning_tree-17490`
18. `minimum_spanning_tree-18769`
19. `minimum_spanning_tree-1922`
20. `minimum_spanning_tree-1944`

## 구현 내용

- 기존 edge/stress 입력과 케이스 순서를 유지했다.
- `data/problems*.json`의 Python 정답 코드를 각 입력에 실행해 expected 문자열을 생성했다.
- 미보장 상태였던 총 85개 override 케이스에 expected를 추가했다.
- oracle failure 회귀 테스트의 정상 사용자 코드를 다음 미완료 문제인 `minimum_spanning_tree-21924`로 이동했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 회귀 테스트:

```text
Ran 9 tests in 3.558s
OK
```

전체 override 품질 감사:

```text
total: 1009
averageQualityScore: 71.86
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 잔여 작업

```text
missing_problem: 178
missing_cases: 653
total_cases: 4531
```

다음 배치는 `minimum_spanning_tree-21924`부터 20개씩 처리한다.
