# Phase 48 - Override Expected Output Batch 32

## 목표

Phase 47 이후 남은 override 중 다음 20개 문제의 모든 케이스에 정적 `expected` 출력을 추가한다.

시뮬레이션과 문자열 문제의 출력 결과를 문제별 Python oracle로 확정해, 채점 시 oracle 재실행 의존성을 줄인다.

## 처리한 문제

1. `simulation-20055`
2. `simulation-20056`
3. `simulation-20058`
4. `simulation-20665`
5. `simulation-21609`
6. `simulation-21610`
7. `simulation-21922`
8. `simulation-22861`
9. `simulation-2933`
10. `simulation-3190`
11. `simulation-5212`
12. `simulation-8972`
13. `string-1032`
14. `string-10798`
15. `string-11365`
16. `string-1152`
17. `string-11720`
18. `string-1181`
19. `string-12871`
20. `string-1316`

## 구현 내용

- 기존 edge/stress 입력과 케이스 순서를 유지했다.
- `data/problems*.json`의 Python 정답 코드를 각 입력에 실행해 expected 문자열을 생성했다.
- 미보장 상태였던 총 95개 override 케이스에 expected를 추가했다.
- 대상 20개에 별도 `check_output` 스페셜 저지가 없음을 생성 전에 확인했다.
- oracle failure 회귀 테스트의 정상 사용자 코드를 다음 미완료 문제인 `string-17609`로 이동했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 회귀 테스트:

```text
Ran 9 tests in 4.368s
OK
```

전체 override 품질 감사:

```text
total: 1009
averageQualityScore: 73.84
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 잔여 작업

```text
missing_problem: 78
missing_cases: 287
total_cases: 4531
```

다음 배치는 `string-17609`부터 20개씩 처리한다.
