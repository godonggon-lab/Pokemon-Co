# Phase 32 - Override Expected Output Batch 16

## 목표

Phase 31 이후 남아 있던 override 중 다음 20개 문제의 `expected` 출력을 고정한다.

이번 배치도 이전과 같은 원칙으로 진행했다.

- 기존 edge/stress 입력은 유지한다.
- 각 override 파일에 `_solve(data: str)`를 추가해 정답 문자열을 생성한다.
- Python/C++ 제출 모두 같은 입력과 expected 출력 기준으로 채점되도록 한다.
- 등록된 정답 코드가 틀린 경우 expected를 틀린 코드에 맞추지 않고, 등록 정답 코드를 수정한다.

## 처리한 문제

1. `dynamic_programming_1-2302`
2. `dynamic_programming_1-2491`
3. `dynamic_programming_1-2565`
4. `dynamic_programming_1-2579`
5. `dynamic_programming_1-2670`
6. `dynamic_programming_1-2876`
7. `dynamic_programming_1-4097`
8. `dynamic_programming_1-9095`
9. `dynamic_programming_1-9461`
10. `dynamic_programming_1-9465`
11. `dynamic_programming_1-9655`
12. `dynamic_programming_2-10653`
13. `dynamic_programming_2-1082`
14. `dynamic_programming_2-10942`
15. `dynamic_programming_2-11049`
16. `dynamic_programming_2-11054`
17. `dynamic_programming_2-11066`
18. `dynamic_programming_2-11909`
19. `dynamic_programming_2-11985`
20. `dynamic_programming_2-12865`

## 구현 메모

- `dynamic_programming_1-2579`의 기존 등록 Python 풀이가 `n=3`에서 세 계단을 모두 밟는 잘못된 답을 냈다.
- 예: `3 / 10 20 15`의 정답은 `35`인데 기존 등록 풀이는 `45`를 출력했다.
- expected를 잘못된 풀이에 맞추지 않고, `data/problems.json`의 등록 풀이를 표준 DP 점화식으로 교체했다.
- `dynamic_programming_1-2302`에 expected가 추가되었기 때문에 oracle failure 단위 테스트 fixture는 다음 미처리 문제인 `dynamic_programming_2-1301`로 이동했다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py \
  dynamic_programming_1-2302 dynamic_programming_1-2491 dynamic_programming_1-2565 \
  dynamic_programming_1-2579 dynamic_programming_1-2670 dynamic_programming_1-2876 \
  dynamic_programming_1-4097 dynamic_programming_1-9095 dynamic_programming_1-9461 \
  dynamic_programming_1-9465 dynamic_programming_1-9655 dynamic_programming_2-10653 \
  dynamic_programming_2-1082 dynamic_programming_2-10942 dynamic_programming_2-11049 \
  dynamic_programming_2-11054 dynamic_programming_2-11066 dynamic_programming_2-11909 \
  dynamic_programming_2-11985 dynamic_programming_2-12865
```

결과:

```text
OK: 20 override files self-judged successfully.
```

추가 검증:

```text
python -m unittest harness.tests.test_judge
```

결과:

```text
Ran 9 tests in 5.759s
OK
```

품질 점검:

```text
npm run judge:quality
```

결과:

```text
total: 1009
averageQualityScore: 67.5
missingStressCount: 0
allHaveOverride: true
```

## Docker Verdict 테스트 상태

Docker Desktop이 켜져 있는 상태에서 전체 `npm run harness:test`를 실행하면 Docker verdict 테스트 2개가 실패했다.

```text
test_cpp_compile_error: timed_out=True
test_output_limit: timed_out=True
```

이번 override expected 검증과 직접 관련된 실패는 아니지만, Docker runner의 compile error/OLE 판정 안정성은 별도 후속 작업으로 확인해야 한다.

## 남은 작업

이번 배치 이후 expected 미보유 override는 다음과 같다.

```text
missing_problem 398
missing_cases 1571
total_cases 4531
```

다음 배치는 `dynamic_programming_2-1301`부터 이어서 처리한다.
