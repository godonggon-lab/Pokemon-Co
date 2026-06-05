# Phase 38 - Override Expected Output Batch 22

## 목표

Phase 37 이후 남아 있던 override 중 다음 20개 문제에 `expected` 출력을 고정한다.

이번 배치도 `data/problems*.json`에 저장된 Python oracle 코드를 실제 실행해 expected 문자열을 고정했다. 기존 edge/stress 입력은 유지하고, 각 입력이 바로 채점 가능한 정답 출력을 갖도록 만드는 작업이다.

## 처리한 문제

1. `graph_traversal-1707`
2. `graph_traversal-17086`
3. `graph_traversal-17129`
4. `graph_traversal-17141`
5. `graph_traversal-1726`
6. `graph_traversal-1743`
7. `graph_traversal-17616`
8. `graph_traversal-18352`
9. `graph_traversal-18404`
10. `graph_traversal-18405`
11. `graph_traversal-1926`
12. `graph_traversal-20924`
13. `graph_traversal-2146`
14. `graph_traversal-2151`
15. `graph_traversal-21937`
16. `graph_traversal-21938`
17. `graph_traversal-2194`
18. `graph_traversal-2206`
19. `graph_traversal-2234`
20. `graph_traversal-22868`

## 구현 메모

- 각 override의 기존 입력을 유지했다.
- 각 입력을 metadata의 Python oracle 코드로 실행해 expected 문자열을 생성했다.
- override 파일은 `edge(input, expected)`, `stress(input, expected)` 형태의 정적 케이스 목록으로 정리했다.
- `graph_traversal-1707`에 expected가 추가되었기 때문에 oracle failure 테스트 fixture는 다음 미보강 문제인 `graph_traversal-22946`으로 이동했다.

## 검증 결과

대상 override 20개 직접 검증:

```text
python scripts/verify-judge-overrides.py \
  graph_traversal-1707 graph_traversal-17086 graph_traversal-17129 \
  graph_traversal-17141 graph_traversal-1726 graph_traversal-1743 \
  graph_traversal-17616 graph_traversal-18352 graph_traversal-18404 \
  graph_traversal-18405 graph_traversal-1926 graph_traversal-20924 \
  graph_traversal-2146 graph_traversal-2151 graph_traversal-21937 \
  graph_traversal-21938 graph_traversal-2194 graph_traversal-2206 \
  graph_traversal-2234 graph_traversal-22868
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
Ran 9 tests in 11.599s
OK
```

품질 점검:

```text
npm run judge:quality
```

결과:

```text
total: 1009
averageQualityScore: 69.88
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

## 남은 작업

이번 배치 이후 expected 미보강 override는 다음과 같다.

```text
missing_problem 278
missing_cases 1136
total_cases 4531
```

다음 배치는 `graph_traversal-22946`부터 이어서 처리한다.
