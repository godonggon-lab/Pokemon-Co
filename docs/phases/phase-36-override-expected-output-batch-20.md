# Phase 36 - Override Expected Output Batch 20

## 목표

Phase 35 이후 남아 있던 override 중 다음 20개 문제에 `expected` 출력을 고정한다.

이번 배치부터는 문제별 정답 로직을 override 안에 다시 옮겨 적는 방식 대신, `data/problems*.json`에 저장된 oracle 코드를 실제로 실행해 각 입력 케이스의 expected 문자열을 고정하는 방식을 사용했다. 이 방식은 현재 케이스에 대해 가장 직접적이고 재현 가능한 정답 근거를 남긴다.

## 처리한 문제

1. `dynamic_programming_2-5582`
2. `dynamic_programming_2-5624`
3. `dynamic_programming_2-9084`
4. `dynamic_programming_2-9251`
5. `dynamic_programming_on_trees-1135`
6. `dynamic_programming_on_trees-12978`
7. `dynamic_programming_on_trees-17831`
8. `dynamic_programming_on_trees-2058`
9. `graph_traversal-10026`
10. `graph_traversal-1012`
11. `graph_traversal-1058`
12. `graph_traversal-10711`
13. `graph_traversal-11123`
14. `graph_traversal-11559`
15. `graph_traversal-11724`
16. `graph_traversal-1240`
17. `graph_traversal-12761`
18. `graph_traversal-12851`
19. `graph_traversal-1303`
20. `graph_traversal-13565`

## 구현 메모

- 각 override의 기존 edge/stress 입력을 유지했다.
- 각 입력을 metadata의 Python oracle 코드로 실행해 expected 문자열을 생성했다.
- override 파일은 `edge(input, expected)`, `stress(input, expected)` 형태의 정적 케이스 목록으로 정리했다.
- `dynamic_programming_2-5582`에 expected가 추가되었기 때문에 oracle failure 테스트 fixture는 다음 미보강 문제인 `graph_traversal-13913`으로 이동했다.
- 이번 방식은 `_solve`를 파일마다 재작성하지 않아도 되어, 문제별 정답 로직을 옮기는 과정의 오타/해석 실수를 줄인다.

## 검증 결과

대상 override 20개 직접 검증:

```text
python scripts/verify-judge-overrides.py \
  dynamic_programming_2-5582 dynamic_programming_2-5624 dynamic_programming_2-9084 \
  dynamic_programming_2-9251 dynamic_programming_on_trees-1135 \
  dynamic_programming_on_trees-12978 dynamic_programming_on_trees-17831 \
  dynamic_programming_on_trees-2058 graph_traversal-10026 graph_traversal-1012 \
  graph_traversal-1058 graph_traversal-10711 graph_traversal-11123 \
  graph_traversal-11559 graph_traversal-11724 graph_traversal-1240 \
  graph_traversal-12761 graph_traversal-12851 graph_traversal-1303 \
  graph_traversal-13565
```

결과:

```text
OK: 20 override files self-judged successfully.
```

judge 핵심 테스트:

```text
python -m unittest harness.tests.test_judge
```

결과:

```text
Ran 9 tests in 13.132s
OK
```

품질 점검:

```text
npm run judge:quality
```

결과:

```text
total: 1009
averageQualityScore: 69.08
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 남은 작업

이번 배치 이후 expected 미보강 override는 다음과 같다.

```text
missing_problem 318
missing_cases 1283
total_cases 4531
```

다음 배치는 `graph_traversal-13913`부터 이어서 처리한다.
