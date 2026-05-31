# Phase 17. Override Expected Output Batch 01

## 목표

override case가 oracle 실행에 의존하지 않도록, 각 override 내부 `_solve`로 expected output을 생성한다. 이 단계는 채점 안정성과 CI 속도를 높이기 위한 첫 배치다.

## 작업 내용

다음 10개 backtracking override에 `_solve`를 추가하고 모든 generated case에 `expected`를 채웠다.

- `backtracking-1038`
- `backtracking-10597`
- `backtracking-10819`
- `backtracking-10974`
- `backtracking-1174`
- `backtracking-1182`
- `backtracking-12101`
- `backtracking-1342`
- `backtracking-1405`
- `backtracking-14712`

## 실행 결과

```bash
python scripts/verify-judge-overrides.py backtracking-1038 backtracking-10597 backtracking-10819 backtracking-10974 backtracking-1174
```

- 5개 모두 `AC`

```bash
python scripts/verify-judge-overrides.py backtracking-1182 backtracking-12101 backtracking-1342 backtracking-1405 backtracking-14712
```

- 5개 모두 `AC`

```bash
npm run judge:quality
npm run harness:test
```

- `averageQualityScore`: 61.55
- `missingStressCount`: 0
- `harness:test`: 20개 테스트 통과

## 다음 단계

- `some_cases_need_oracle`가 남은 backtracking 문제를 계속 줄인다.
- 단순 완전탐색으로 expected를 만들 수 있는 문제부터 처리한다.
- 출력이 매우 큰 문제는 `_solve` 방식은 유지하되 케이스 크기를 CI 친화적으로 제한한다.
