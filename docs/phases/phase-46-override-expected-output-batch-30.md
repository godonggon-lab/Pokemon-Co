# Phase 46 - Override Expected Output Batch 30

## 목표

Phase 45 이후 남은 override 중 다음 20개 문제의 모든 케이스에 정적 `expected` 출력을 추가한다.

최단경로와 시뮬레이션 문제의 상태 전이 결과를 문제별 Python oracle로 확정해, 제출 언어와 무관한 채점 기준을 유지한다.

## 처리한 문제

1. `shortest_path-20183`
2. `shortest_path-21940`
3. `shortest_path-2211`
4. `shortest_path-2224`
5. `shortest_path-22865`
6. `shortest_path-22870`
7. `shortest_path-2307`
8. `shortest_path-2458`
9. `shortest_path-2660`
10. `shortest_path-2982`
11. `shortest_path-4485`
12. `shortest_path-5972`
13. `shortest_path-9205`
14. `shortest_path-9370`
15. `simulation-13459`
16. `simulation-13460`
17. `simulation-14499`
18. `simulation-14594`
19. `simulation-14891`
20. `simulation-15644`

## 구현 내용

- 기존 edge/stress 입력과 케이스 순서를 유지했다.
- `data/problems*.json`의 Python 정답 코드를 각 입력에 실행해 expected 문자열을 생성했다.
- 미보장 상태였던 총 65개 override 케이스에 expected를 추가했다.
- `simulation-15644`는 여러 정답 경로를 허용해야 하므로 기존 `check_output` 스페셜 저지를 유지했다.
- oracle failure 회귀 테스트의 정상 사용자 코드를 다음 미완료 문제인 `simulation-15653`으로 이동했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 회귀 테스트:

```text
Ran 9 tests in 3.066s
OK
```

전체 override 품질 감사:

```text
total: 1009
averageQualityScore: 73.05
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 잔여 작업

```text
missing_problem: 118
missing_cases: 447
total_cases: 4531
```

다음 배치는 `simulation-15653`부터 20개씩 처리한다.
