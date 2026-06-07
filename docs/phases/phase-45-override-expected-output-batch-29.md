# Phase 45 - Override Expected Output Batch 29

## 목표

Phase 44 이후 남은 override 중 다음 20개 문제의 모든 케이스에 정적 `expected` 출력을 추가한다.

최단경로 문제의 다양한 출력 형식을 문제별 Python oracle로 확정해, 제출 언어와 무관한 채점 기준을 유지한다.

## 처리한 문제

1. `shortest_path-1277`
2. `shortest_path-13424`
3. `shortest_path-1389`
4. `shortest_path-13911`
5. `shortest_path-1445`
6. `shortest_path-1446`
7. `shortest_path-14938`
8. `shortest_path-1504`
9. `shortest_path-15723`
10. `shortest_path-16118`
11. `shortest_path-1613`
12. `shortest_path-1719`
13. `shortest_path-1753`
14. `shortest_path-18223`
15. `shortest_path-18243`
16. `shortest_path-1865`
17. `shortest_path-1916`
18. `shortest_path-1956`
19. `shortest_path-20168`
20. `shortest_path-20182`

## 구현 내용

- 기존 edge/stress 입력과 케이스 순서를 유지했다.
- `data/problems*.json`의 Python 정답 코드를 각 입력에 실행해 expected 문자열을 생성했다.
- 미보장 상태였던 총 62개 override 케이스에 expected를 추가했다.
- oracle failure 회귀 테스트의 정상 사용자 코드를 다음 미완료 문제인 `shortest_path-20183`으로 이동했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 회귀 테스트:

```text
Ran 9 tests in 3.258s
OK
```

전체 override 품질 감사:

```text
total: 1009
averageQualityScore: 72.65
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 잔여 작업

```text
missing_problem: 138
missing_cases: 512
total_cases: 4531
```

다음 배치는 `shortest_path-20183`부터 20개씩 처리한다.
