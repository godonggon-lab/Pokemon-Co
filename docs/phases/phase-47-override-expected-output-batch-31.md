# Phase 47 - Override Expected Output Batch 31

## 목표

Phase 46 이후 남은 override 중 다음 20개 문제의 모든 케이스에 정적 `expected` 출력을 추가한다.

시뮬레이션 문제의 복잡한 상태 전이 결과를 문제별 Python oracle로 확정해, 실행 시점의 oracle 의존성을 줄인다.

## 처리한 문제

1. `simulation-15653`
2. `simulation-15683`
3. `simulation-15685`
4. `simulation-16234`
5. `simulation-16235`
6. `simulation-16939`
7. `simulation-1713`
8. `simulation-17135`
9. `simulation-17140`
10. `simulation-17143`
11. `simulation-17779`
12. `simulation-17780`
13. `simulation-17822`
14. `simulation-17837`
15. `simulation-18500`
16. `simulation-18809`
17. `simulation-19235`
18. `simulation-19236`
19. `simulation-19237`
20. `simulation-19238`

## 구현 내용

- 기존 edge/stress 입력과 케이스 순서를 유지했다.
- `data/problems*.json`의 Python 정답 코드를 각 입력에 실행해 expected 문자열을 생성했다.
- 미보장 상태였던 총 65개 override 케이스에 expected를 추가했다.
- 대상 20개에 별도 `check_output` 스페셜 저지가 없음을 생성 전에 확인했다.
- oracle failure 회귀 테스트의 정상 사용자 코드를 다음 미완료 문제인 `simulation-20055`로 이동했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 회귀 테스트:

```text
Ran 9 tests in 13.630s
OK
```

전체 override 품질 감사:

```text
total: 1009
averageQualityScore: 73.44
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 잔여 작업

```text
missing_problem: 98
missing_cases: 382
total_cases: 4531
```

다음 배치는 `simulation-20055`부터 20개씩 처리한다.
