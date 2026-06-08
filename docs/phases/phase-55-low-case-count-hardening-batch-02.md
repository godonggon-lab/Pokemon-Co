# Phase 55 - Low Case Count Hardening Batch 02

## 목표

`case_count_lt_6` 품질 gap을 줄이기 위해 backtracking override 20개를 최소 6케이스로 보강한다.

## 처리한 문제

1. `backtracking-16922`
2. `backtracking-16938`
3. `backtracking-16987`
4. `backtracking-17136`
5. `backtracking-1729`
6. `backtracking-1759`
7. `backtracking-1799`
8. `backtracking-18290`
9. `backtracking-18429`
10. `backtracking-1941`
11. `backtracking-19699`
12. `backtracking-1987`
13. `backtracking-19942`
14. `backtracking-19949`
15. `backtracking-20208`
16. `backtracking-2023`
17. `backtracking-20950`
18. `backtracking-2239`
19. `backtracking-2529`
20. `backtracking-2661`

## 구현 내용

- 각 문제를 최소 6개 edge/stress 케이스로 보강했다.
- 최소 입력, 불가능한 조합, 중복값, 음수, 단일 해, 경계값을 문제 특성에 맞게 추가했다.
- 기존 `_solve()` 기반 expected 생성 구조는 유지했다.
- 조합 탐색 비용이 큰 문제는 작은 입력이나 이미 진행된 상태를 사용해 self-judge 시간이 과도하게 늘지 않게 했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 단위 테스트:

```text
Ran 9 tests in 5.315s
OK
```

override 품질 감사:

```text
averageQualityScore: 76.38
lowQualityCount: 551
missingStressCount: 0
allHaveOverride: true
```

직접 집계:

```text
case_count_lt_6: 573 -> 553
```

Python 문법 검사:

```text
py_compile 통과
```

## 다음 작업

다음 배치는 `backtracking-2922`부터 남은 backtracking 문제와 binary search 문제를 이어서 보강한다.
