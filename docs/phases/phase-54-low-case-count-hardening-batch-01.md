# Phase 54 - Low Case Count Hardening Batch 01

## 목표

Phase 53 이후 남은 품질 gap 중 `case_count_lt_6`를 줄인다.

이 단계부터는 모든 override가 expected를 갖춘 상태에서, 케이스 수가 6개 미만인 문제를 우선 보강한다. 첫 배치는 backtracking 문제 20개를 대상으로 했다.

## 처리한 문제

1. `backtracking-10421`
2. `backtracking-10597`
3. `backtracking-1062`
4. `backtracking-10819`
5. `backtracking-10971`
6. `backtracking-1174`
7. `backtracking-12101`
8. `backtracking-1248`
9. `backtracking-12908`
10. `backtracking-1342`
11. `backtracking-13908`
12. `backtracking-1469`
13. `backtracking-14888`
14. `backtracking-1497`
15. `backtracking-1553`
16. `backtracking-15566`
17. `backtracking-15659`
18. `backtracking-15684`
19. `backtracking-15918`
20. `backtracking-16571`

## 구현 내용

- 대상 20개 override를 모두 최소 6케이스로 보강했다.
- 기존 `_solve()` 기반 expected 생성 구조는 유지했다.
- `backtracking-15566`은 특수 채점 문제이므로 기존 `check_output`을 보존하고, 새 케이스도 expected는 빈 문자열로 유지했다.
- 검증 과정에서 발견한 입력 안정성 이슈를 함께 수정했다.
  - `backtracking-10597`: reference 풀이가 길이 9 미만 입력을 처리하지 않아, 문제 제약에 맞는 1~9 이상 순열 입력으로 교체했다.
  - `backtracking-1553`: 도미노 문제는 숫자 0~6만 유효하므로 7이 포함된 잘못된 테스트 입력을 제거했다.
  - `backtracking-16571`: 빈 틱택토 보드는 reference 풀이가 시간 초과되어, 이미 일부 진행된 보드 케이스로 교체했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 단위 테스트:

```text
Ran 9 tests in 11.103s
OK
```

override 품질 감사:

```text
averageQualityScore: 75.88
lowQualityCount: 571
missingStressCount: 0
allHaveOverride: true
```

직접 집계:

```text
case_count_lt_6: 593 -> 573
```

Python 문법 검사:

```text
py_compile 통과
```

## 다음 작업

다음 배치는 `backtracking-16922`부터 이어서 20개를 최소 6케이스로 보강한다.
