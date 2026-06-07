# Phase 51 - Override Expected Output Batch 35

## 목표

Phase 50 이후 남아 있던 override 중 다음 20개 문제의 채점 입력을 정적 expected 기반으로 안정화한다.

이번 배치는 트리, 트라이, 투포인터 문제가 섞여 있다. 모두 출력이 고정되는 문제로 판단되어 Python 정답 코드를 oracle로 실행한 결과를 각 override 케이스의 `expected`로 저장했다.

## 처리한 문제

1. `tree-4933`
2. `tree-5639`
3. `tree-6416`
4. `tree-9372`
5. `tree-9489`
6. `trie-14725`
7. `trie-19585`
8. `trie-20166`
9. `trie-5052`
10. `trie-5446`
11. `trie-5670`
12. `trie-9202`
13. `two_pointer-10025`
14. `two_pointer-1484`
15. `two_pointer-14921`
16. `two_pointer-15565`
17. `two_pointer-15831`
18. `two_pointer-15961`
19. `two_pointer-1644`
20. `two_pointer-16472`

## 구현 내용

- 총 69개 override 케이스에 정적 `expected` 출력을 추가했다.
- 기존 edge/stress 입력의 순서와 종류는 유지했다.
- 이번 대상 20개에는 별도 `check_output` 특수 채점이 필요한 문제는 없었다.
- oracle failure 단위 테스트의 fixture를 이번 배치에서 완료된 `tree-4933`에서 다음 미완료 문제인 `two_pointer-1806`으로 옮겼다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 단위 테스트:

```text
Ran 9 tests in 2.576s
OK
```

override 품질 감사:

```text
total: 1009
averageQualityScore: 75.03
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
missing_problem: 18
missing_cases: 74
total_cases: 4531
```

다음 배치는 `two_pointer-1806`부터 남은 18개를 처리한다.
