# Phase 56 - Low Case Count Hardening Batch 03

## 목표

`case_count_lt_6` 품질 gap을 줄이기 위해 backtracking/binary_search override 20개를 최소 6케이스로 보강한다.

## 처리한 문제

1. `backtracking-2922`
2. `backtracking-3165`
3. `backtracking-3980`
4. `backtracking-6443`
5. `backtracking-6603`
6. `backtracking-6987`
7. `backtracking-7490`
8. `backtracking-7682`
9. `backtracking-9944`
10. `binary_search-1072`
11. `binary_search-11561`
12. `binary_search-1166`
13. `binary_search-11663`
14. `binary_search-11687`
15. `binary_search-12757`
16. `binary_search-1300`
17. `binary_search-13397`
18. `binary_search-13702`
19. `binary_search-14575`
20. `binary_search-14627`

## 구현 내용

- 각 문제를 최소 6개 edge/stress 케이스로 보강했다.
- backtracking 문제는 작은 탐색 공간 위주로 케이스를 추가해 검증 시간이 폭증하지 않게 했다.
- binary search 문제는 최소/최대, 불가능에 가까운 값, 중복값, 경계 쿼리 등을 추가했다.
- 검증 중 발견한 입력 안정성 이슈를 함께 수정했다.
  - `backtracking-3980`: 11x11 all-one 능력치 케이스가 reference 풀이에서 TLE를 유발해 sparse paired 케이스로 교체했다.
  - `binary_search-14627`: 불가능한 목표 개수에서 reference 풀이가 `ans` 미정의 RE를 내므로, 가능한 경계 입력으로 교체했다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 20 override files self-judged successfully.
```

judge 단위 테스트:

```text
Ran 9 tests in 4.963s
OK
```

override 품질 감사:

```text
averageQualityScore: 76.87
lowQualityCount: 531
missingStressCount: 0
allHaveOverride: true
```

직접 집계:

```text
case_count_lt_6: 553 -> 533
```

Python 문법 검사:

```text
py_compile 통과
```

## 다음 작업

다음 배치는 `binary_search-1561`부터 이어서 binary search 문제를 보강한다.
