# Phase 50 - Override Expected Output Batch 34

## 목표

Phase 49 이후 남아 있던 override 중 다음 20개 트리 문제의 채점 입력을 정적 expected 기반으로 안정화한다.

이번 배치는 모두 단일 정답 형태의 출력으로 판단되어, Python 정답 코드를 oracle로 실행해 각 override 케이스의 `expected` 값을 고정했다.

## 처리한 문제

1. `tree-12912`
2. `tree-14267`
3. `tree-14570`
4. `tree-14657`
5. `tree-14675`
6. `tree-15681`
7. `tree-15900`
8. `tree-1595`
9. `tree-16437`
10. `tree-17073`
11. `tree-19535`
12. `tree-19542`
13. `tree-19581`
14. `tree-19641`
15. `tree-20364`
16. `tree-2233`
17. `tree-2250`
18. `tree-2263`
19. `tree-4315`
20. `tree-4803`

## 구현 내용

- 총 62개 override 케이스에 정적 `expected` 출력을 추가했다.
- 기존 edge/stress 입력의 순서와 종류는 유지했다.
- 이번 대상 20개에는 별도 `check_output` 특수 채점이 필요한 문제는 없었다.
- oracle failure 단위 테스트의 fixture를 이번 배치에서 완료된 `tree-12912`에서 다음 미완료 문제인 `tree-4933`으로 옮겼다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 단위 테스트:

```text
Ran 9 tests in 3.685s
OK
```

override 품질 감사:

```text
total: 1009
averageQualityScore: 74.63
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

Python 문법 검사:

```text
py_compile 통과
```

## 남은 작업

```text
missing_problem: 38
missing_cases: 143
total_cases: 4531
```

다음 배치는 `tree-4933`부터 20개씩 이어서 처리한다.
