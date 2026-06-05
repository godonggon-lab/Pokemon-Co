# Phase 37 - Override Expected Output Batch 21

## 목표

Phase 36 이후 남아 있던 override 중 다음 20개 문제에 `expected` 출력을 고정한다.

이번 배치도 `data/problems*.json`에 저장된 Python oracle 코드를 실제 실행해 expected 문자열을 고정했다. 이 방식은 각 override의 기존 edge/stress 입력을 유지하면서도, 현재 케이스에 대한 정답 출력을 가장 직접적으로 보존한다.

## 처리한 문제

1. `graph_traversal-13913`
2. `graph_traversal-14248`
3. `graph_traversal-14442`
4. `graph_traversal-14496`
5. `graph_traversal-14502`
6. `graph_traversal-14716`
7. `graph_traversal-14923`
8. `graph_traversal-15558`
9. `graph_traversal-1600`
10. `graph_traversal-16432`
11. `graph_traversal-16928`
12. `graph_traversal-16932`
13. `graph_traversal-16947`
14. `graph_traversal-16948`
15. `graph_traversal-16953`
16. `graph_traversal-16954`
17. `graph_traversal-16956`
18. `graph_traversal-16973`
19. `graph_traversal-16985`
20. `graph_traversal-16988`

## 구현 메모

- 각 override의 기존 입력은 유지했다.
- 각 입력을 metadata의 Python oracle 코드로 실행해 expected 문자열을 생성했다.
- override 파일은 `edge(input, expected)`, `stress(input, expected)` 형태의 정적 케이스 목록으로 정리했다.
- `graph_traversal-13913`에 expected가 추가되었기 때문에 oracle failure 테스트 fixture는 다음 미보강 문제인 `graph_traversal-1707`로 이동했다.

## 검증 결과

대상 override 20개 직접 검증:

```text
python scripts/verify-judge-overrides.py \
  graph_traversal-13913 graph_traversal-14248 graph_traversal-14442 \
  graph_traversal-14496 graph_traversal-14502 graph_traversal-14716 \
  graph_traversal-14923 graph_traversal-15558 graph_traversal-1600 \
  graph_traversal-16432 graph_traversal-16928 graph_traversal-16932 \
  graph_traversal-16947 graph_traversal-16948 graph_traversal-16953 \
  graph_traversal-16954 graph_traversal-16956 graph_traversal-16973 \
  graph_traversal-16985 graph_traversal-16988
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
Ran 9 tests in 13.412s
OK
```

품질 점검:

```text
npm run judge:quality
```

결과:

```text
total: 1009
averageQualityScore: 69.48
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 남은 작업

이번 배치 이후 expected 미보강 override는 다음과 같다.

```text
missing_problem 298
missing_cases 1211
total_cases 4531
```

다음 배치는 `graph_traversal-1707`부터 이어서 처리한다.
