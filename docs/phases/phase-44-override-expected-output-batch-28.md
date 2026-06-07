# Phase 44 - Override Expected Output Batch 28

## 목표

Phase 43 이후 남은 override 중 다음 20개 문제의 모든 케이스에 정적 `expected` 출력을 추가한다.

정적 expected를 통해 제출 언어와 무관한 입력/정답 계약을 유지하고, 실제 채점 중 oracle 실행 실패 가능성을 줄인다.

## 처리한 문제

1. `minimum_spanning_tree-21924`
2. `minimum_spanning_tree-2406`
3. `minimum_spanning_tree-2887`
4. `minimum_spanning_tree-4386`
5. `minimum_spanning_tree-6497`
6. `prefix_sum-11659`
7. `prefix_sum-20116`
8. `prefix_sum-2015`
9. `prefix_sum-20159`
10. `shortest_path-10159`
11. `shortest_path-10282`
12. `shortest_path-11265`
13. `shortest_path-11403`
14. `shortest_path-11404`
15. `shortest_path-11562`
16. `shortest_path-11657`
17. `shortest_path-11779`
18. `shortest_path-11780`
19. `shortest_path-1219`
20. `shortest_path-1261`

## 구현 내용

- 기존 edge/stress 입력과 케이스 순서를 유지했다.
- `data/problems*.json`의 Python 정답 코드를 각 입력에 실행해 expected 문자열을 생성했다.
- 미보장 상태였던 총 79개 override 케이스에 expected를 추가했다.
- oracle failure 회귀 테스트의 정상 사용자 코드를 다음 미완료 문제인 `shortest_path-1277`로 이동했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 회귀 테스트:

```text
Ran 9 tests in 2.600s
OK
```

전체 override 품질 감사:

```text
total: 1009
averageQualityScore: 72.25
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 잔여 작업

```text
missing_problem: 158
missing_cases: 574
total_cases: 4531
```

다음 배치는 `shortest_path-1277`부터 20개씩 처리한다.
