# Phase 39 - Override Expected Output Batch 23

## 목표

Phase 38 이후 남아 있던 override 중 다음 20개 문제에 `expected` 출력을 고정한다.

이번 배치도 `data/problems*.json`에 저장된 Python oracle 코드를 실제 실행해 expected 문자열을 생성했다. 기존 edge/stress 입력을 유지하면서 각 입력이 바로 채점 가능한 정답 출력을 갖도록 한다.

## 처리한 문제

1. `graph_traversal-22946`
2. `graph_traversal-22948`
3. `graph_traversal-22949`
4. `graph_traversal-2583`
5. `graph_traversal-2589`
6. `graph_traversal-2644`
7. `graph_traversal-2665`
8. `graph_traversal-2668`
9. `graph_traversal-3055`
10. `graph_traversal-3184`
11. `graph_traversal-3187`
12. `graph_traversal-4179`
13. `graph_traversal-4963`
14. `graph_traversal-5014`
15. `graph_traversal-5427`
16. `graph_traversal-5567`
17. `graph_traversal-6087`
18. `graph_traversal-6118`
19. `graph_traversal-7562`
20. `graph_traversal-7569`

## 구현 메모

- 각 override의 기존 입력을 유지했다.
- 각 입력을 metadata의 Python oracle 코드로 실행해 expected 문자열을 생성했다.
- override 파일은 `edge(input, expected)`, `stress(input, expected)` 형태의 정적 케이스 목록으로 정리했다.
- `graph_traversal-22946`에 expected가 추가되었기 때문에 oracle failure 테스트 fixture는 다음 미보강 문제인 `graph_traversal-9019`로 이동했다.

## 검증 결과

대상 override 20개 직접 검증:

```text
python scripts/verify-judge-overrides.py \
  graph_traversal-22946 graph_traversal-22948 graph_traversal-22949 \
  graph_traversal-2583 graph_traversal-2589 graph_traversal-2644 \
  graph_traversal-2665 graph_traversal-2668 graph_traversal-3055 \
  graph_traversal-3184 graph_traversal-3187 graph_traversal-4179 \
  graph_traversal-4963 graph_traversal-5014 graph_traversal-5427 \
  graph_traversal-5567 graph_traversal-6087 graph_traversal-6118 \
  graph_traversal-7562 graph_traversal-7569
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
Ran 9 tests in 2.196s
OK
```

품질 점검:

```text
npm.cmd run judge:quality
```

결과:

```text
total: 1009
averageQualityScore: 70.27
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 남은 작업

이번 배치 이후 expected 미보강 override는 다음과 같다.

```text
missing_problem 258
missing_cases 1057
total_cases 4531
```

다음 배치는 `graph_traversal-9019`부터 이어서 처리한다.
