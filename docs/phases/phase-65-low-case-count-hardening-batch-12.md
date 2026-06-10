# Phase 65 - Low Case Count Hardening Batch 12

## 목표

`case_count_lt_6` 품질 경고가 남아 있던 `dynamic_programming_1-2565`부터
`dynamic_programming_2-14863`까지 20개 override를 보강한다.

완료 기준은 다음과 같다.

- 각 override가 최소 6개의 입력 케이스를 가진다.
- 추가 입력이 문제의 입력 제약과 형식을 지킨다.
- 모든 기대 출력은 문제별 oracle로 생성한다.
- reference solution self-judge가 모든 케이스에서 AC를 받는다.
- 공통 judge 회귀 테스트와 Python 문법 검사가 통과한다.

## 처리한 문제

- `dynamic_programming_1-2565`
- `dynamic_programming_1-2670`
- `dynamic_programming_1-2876`
- `dynamic_programming_1-4097`
- `dynamic_programming_2-10653`
- `dynamic_programming_2-1082`
- `dynamic_programming_2-10942`
- `dynamic_programming_2-11049`
- `dynamic_programming_2-11054`
- `dynamic_programming_2-11066`
- `dynamic_programming_2-12865`
- `dynamic_programming_2-1301`
- `dynamic_programming_2-13302`
- `dynamic_programming_2-13398`
- `dynamic_programming_2-13707`
- `dynamic_programming_2-13902`
- `dynamic_programming_2-14226`
- `dynamic_programming_2-14699`
- `dynamic_programming_2-14728`
- `dynamic_programming_2-14863`

## 구현 내용

- LIS 계열 문제에는 완전 증가, 완전 감소, 중복 값, 정렬되지 않은 입력을 추가했다.
- 연속 부분 수열 문제에는 전체 음수, 중간 단절, 삭제 전후 최댓값이 달라지는 입력을 보강했다.
- 배낭과 선택 DP에는 동일 무게, 정확한 용량 조합, 단일 항목 선택이 오답을 드러내는 입력을 추가했다.
- 구간 DP에는 팰린드롬의 홀수·짝수 길이와 행렬 및 파일 결합 순서가 결과를 바꾸는 입력을 추가했다.
- 상태 DP에는 불가능 상태, 동일 비용의 자리 선택, 쿠폰 및 건너뛰기 사용 경계를 보강했다.
- 기존 stress 케이스는 유지하면서 각 override를 정확히 6개 케이스로 구성했다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py <batch 12 slugs>
OK: 20 override files self-judged successfully.
각 문제: python AC 6/6
```

```text
python -m unittest harness.tests.test_judge
Ran 9 tests in 2.470s
OK
```

```text
npm.cmd run judge:quality
total: 1009
averageQualityScore: 81.33
lowQualityCount: 352
missingStressCount: 0
allHaveOverride: true
```

```text
python -m py_compile <batch 12 override files>
OK
```

## 작업 결과

- 저품질 override 수가 `372 -> 352`로 20개 감소했다.
- 평균 품질 점수가 `80.84 -> 81.33`으로 상승했다.
- 이번 배치의 20개 override는 모두 최소 6개 케이스와 stress 케이스를 가진다.
- 다음 일반 배치는 `dynamic_programming_2-14925`부터 이어서 처리한다.
