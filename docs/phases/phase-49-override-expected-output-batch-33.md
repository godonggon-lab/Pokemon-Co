# Phase 49 - Override Expected Output Batch 33

## 목표

Phase 48 이후 남아 있던 override 중 다음 20개 문제의 채점 안정성을 높인다.

이번 배치는 문자열, 위상정렬, 트리 문제의 입력 케이스를 다뤘다. 대부분은 Python 정답 코드를 oracle로 실행해 정적 `expected` 출력을 추가했고, 복수 정답이 가능한 위상정렬 문제는 문자열 고정 비교 대신 특수 채점으로 처리했다.

## 처리한 문제

1. `string-17609`
2. `string-20154`
3. `string-2204`
4. `string-2744`
5. `string-2922`
6. `string-3029`
7. `string-9046`
8. `string-9342`
9. `topological_sorting-14676`
10. `topological_sorting-1766`
11. `topological_sorting-1948`
12. `topological_sorting-20119`
13. `topological_sorting-21276`
14. `topological_sorting-2252`
15. `topological_sorting-2623`
16. `topological_sorting-3665`
17. `topological_sorting-9470`
18. `tree-1167`
19. `tree-1240`
20. `tree-12896`

## 구현 내용

- 총 82개 override 케이스를 처리했다.
- `string-*`, 대부분의 `topological_sorting-*`, `tree-*` 문제는 Python oracle 출력으로 정적 `expected`를 추가했다.
- `topological_sorting-2252`는 정답 순서가 여러 개 가능하므로 `check_output`에서 다음을 검증한다.
  - 출력이 1부터 N까지의 순열인지
  - 모든 `a -> b` 제약에서 `a`가 `b`보다 먼저 나오는지
- `topological_sorting-2623`도 가능한 위상정렬이 여러 개일 수 있으므로 `check_output`에서 다음을 검증한다.
  - 사이클이 있으면 출력이 `0`인지
  - 사이클이 없으면 출력이 1부터 N까지의 순열이고 모든 PD 순서 제약을 만족하는지
- oracle failure 단위 테스트의 fixture를 이번 배치에서 완료된 `string-17609`에서 다음 미완료 문제인 `tree-12912`로 옮겼다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 단위 테스트:

```text
Ran 9 tests in 4.711s
OK
```

override 품질 감사:

```text
total: 1009
averageQualityScore: 74.24
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
missing_problem: 58
missing_cases: 205
total_cases: 4531
```

다음 배치는 `tree-12912`부터 20개씩 이어서 처리한다.
