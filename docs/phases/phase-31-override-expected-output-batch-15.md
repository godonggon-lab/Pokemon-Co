# Phase 31 - Override Expected Output Batch 15

## 목표

Phase 30 이후 남아 있던 override 중 다음 20개 문제의 `expected` 출력을 문제별 oracle 함수로 고정한다.

이번 배치의 기준은 다음과 같다.

- 기존 `gen_inputs`의 edge/stress 입력은 유지한다.
- 각 override 파일 안에 `_solve(data: str)`를 추가해 입력별 정답 문자열을 생성한다.
- 사용자 제출 언어가 Python/C++ 중 무엇이든 같은 입력/출력 기준으로 채점되도록 한다.
- expected가 채워진 문제는 oracle 실행 없이도 결정적으로 비교할 수 있게 한다.

## 처리한 문제

1. `dynamic_programming_1-16194`
2. `dynamic_programming_1-16195`
3. `dynamic_programming_1-1633`
4. `dynamic_programming_1-1660`
5. `dynamic_programming_1-1699`
6. `dynamic_programming_1-17175`
7. `dynamic_programming_1-17212`
8. `dynamic_programming_1-17291`
9. `dynamic_programming_1-17626`
10. `dynamic_programming_1-18353`
11. `dynamic_programming_1-1932`
12. `dynamic_programming_1-19622`
13. `dynamic_programming_1-1965`
14. `dynamic_programming_1-2011`
15. `dynamic_programming_1-20152`
16. `dynamic_programming_1-20162`
17. `dynamic_programming_1-2193`
18. `dynamic_programming_1-22857`
19. `dynamic_programming_1-22869`
20. `dynamic_programming_1-2294`

## 구현 메모

- `dynamic_programming_1-17291`은 첫 구현에서 기존 등록 정답과 recurrence가 달라 target verification에서 WA가 났다.
- 원 import 코드의 출생/사망 계산 방식으로 `_solve`를 맞춘 뒤 재검증에서 AC를 확인했다.
- `dynamic_programming_1-16195`에 expected가 추가되었기 때문에, oracle failure 단위 테스트 fixture는 다음 미처리 문제인 `dynamic_programming_1-2302`로 이동했다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py \
  dynamic_programming_1-16194 dynamic_programming_1-16195 dynamic_programming_1-1633 \
  dynamic_programming_1-1660 dynamic_programming_1-1699 dynamic_programming_1-17175 \
  dynamic_programming_1-17212 dynamic_programming_1-17291 dynamic_programming_1-17626 \
  dynamic_programming_1-18353 dynamic_programming_1-1932 dynamic_programming_1-19622 \
  dynamic_programming_1-1965 dynamic_programming_1-2011 dynamic_programming_1-20152 \
  dynamic_programming_1-20162 dynamic_programming_1-2193 dynamic_programming_1-22857 \
  dynamic_programming_1-22869 dynamic_programming_1-2294
```

결과:

```text
OK: 20 override files self-judged successfully.
```

추가 검증:

```text
npm run harness:test
```

결과:

```text
Ran 20 tests in 13.713s
OK (skipped=5)
```

Docker verdict 테스트 5개는 현재 로컬 Docker daemon이 꺼져 있어 skip 처리되었다.

```text
npm run judge:quality
```

결과:

```text
total: 1009
averageQualityScore: 67.1
missingStressCount: 0
allHaveOverride: true
```

## 남은 작업

이번 배치 이후 expected 미보유 override는 다음과 같다.

```text
missing_problem 418
missing_cases 1660
total_cases 4531
```

다음 배치는 `dynamic_programming_1-2302`부터 이어서 처리한다.
