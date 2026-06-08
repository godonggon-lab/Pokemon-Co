# Phase 52 - Override Expected Output Final Batch

## 목표

Phase 51 이후 남아 있던 마지막 18개 override 문제를 처리해, 모든 override 케이스가 정적 `expected` 또는 특수 채점 기준을 갖도록 마무리한다.

이번 배치는 모두 투포인터 문제이며, 출력이 단일 값으로 고정되는 문제로 판단되어 Python 정답 코드를 oracle로 실행한 결과를 각 override 케이스의 `expected`로 저장했다.

## 처리한 문제

1. `two_pointer-1806`
2. `two_pointer-1940`
3. `two_pointer-2003`
4. `two_pointer-2018`
5. `two_pointer-20366`
6. `two_pointer-20442`
7. `two_pointer-2118`
8. `two_pointer-21279`
9. `two_pointer-21921`
10. `two_pointer-22862`
11. `two_pointer-2428`
12. `two_pointer-2473`
13. `two_pointer-2531`
14. `two_pointer-2559`
15. `two_pointer-3151`
16. `two_pointer-3273`
17. `two_pointer-6137`
18. `two_pointer-6159`

## 구현 내용

- 총 74개 override 케이스에 정적 `expected` 출력을 추가했다.
- 기존 edge/stress 입력의 순서와 종류는 유지했다.
- 모든 override의 expected 미완료 케이스가 0개가 되었기 때문에, oracle failure 단위 테스트를 실제 미완료 문제에 의존하지 않는 구조로 바꿨다.
  - `no_samples-999998` 가짜 문제 slug를 사용한다.
  - 테스트 내부에서만 `generators.generate`를 임시로 교체해 expected가 없는 1개 입력을 만든다.
  - bad oracle이 실행 실패할 때 `ERR`와 `oracle failed` 메시지가 나오는지 검증한다.

## 검증 결과

대상 override 자체 채점:

```text
OK: 18 override files self-judged successfully.
```

judge 단위 테스트:

```text
Ran 9 tests in 8.100s
OK
```

override 품질 감사:

```text
total: 1009
averageQualityScore: 75.39
lowQualityCount: 591
missingStressCount: 0
allHaveOverride: true
```

coverage 감사:

```text
total: 1009
judgeReady: 1009
missingCases: 0
overrides: 1009
sampleOnly: 0
highRiskSampleOnly: 0
```

Python 문법 검사:

```text
py_compile 통과
```

전체 override self-judge:

```text
npm run judge:verify-overrides
```

위 명령은 10분 제한에서 타임아웃되었다. 대상 18개 self-judge, 전체 coverage 감사, 전체 quality 감사는 통과했지만, 전체 1009개를 한 번에 실행하는 검증은 시간이 오래 걸리므로 이후에는 CI/nightly에서 분할 실행하는 방식이 필요하다.

## 최종 상태

```text
missing_problem: 0
missing_cases: 0
total_cases: 4531
```

이 단계로 “override expected 미완료 제거” 작업은 완료되었다. 다음 작업은 케이스 개수가 적은 문제의 edge/stress 보강과, 전체 self-judge를 배치 단위로 실행하는 CI 개선이다.
