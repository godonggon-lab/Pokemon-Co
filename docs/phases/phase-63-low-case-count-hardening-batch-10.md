# Phase 63 - Low Case Count Hardening Batch 10

## 목표

낮은 케이스 수(`case_count_lt_6`)로 남아 있던 실제 품질 대상 중 `divide_and_conquer-2448`부터 `dynamic_programming_1-15624`까지 20개를 보강했다.

이번 단계의 기준은 다음과 같다.

- 각 override가 최소 6개 이상의 입력 케이스를 가진다.
- 추가 케이스는 문제 제약 안에서 구성한다.
- 출력은 override 내부 oracle로 생성한다.
- Python과 C++ reference solution 기준 self-judge가 모두 AC여야 한다.

## 처리한 문제

- `divide_and_conquer-2448`
- `dynamic_programming_1-1003`
- `dynamic_programming_1-10211`
- `dynamic_programming_1-10844`
- `dynamic_programming_1-11051`
- `dynamic_programming_1-11052`
- `dynamic_programming_1-11057`
- `dynamic_programming_1-11060`
- `dynamic_programming_1-1149`
- `dynamic_programming_1-11568`
- `dynamic_programming_1-12026`
- `dynamic_programming_1-1309`
- `dynamic_programming_1-13910`
- `dynamic_programming_1-14430`
- `dynamic_programming_1-1446`
- `dynamic_programming_1-14852`
- `dynamic_programming_1-1495`
- `dynamic_programming_1-1535`
- `dynamic_programming_1-15489`
- `dynamic_programming_1-15624`

## 구현 내용

- 수열 DP에는 최소 입력, 전부 음수, 반복 값, 도달 불가, 단조 증가/감소 케이스를 추가했다.
- 배낭 및 상태 전이 문제에는 용량 경계, 상태 소진, 선택 불가능 케이스를 추가했다.
- 별 찍기 문제는 허용되는 높이인 48과 96을 추가해 재귀 깊이와 출력 크기를 보강했다.
- 기존 stress 케이스는 유지하고 edge 케이스를 추가해 최소 6개 케이스를 맞췄다.

## Docker 확인

첫 self-judge에서 Docker Desktop 엔진이 꺼져 있어 C++ reference인 `divide_and_conquer-2448`이 RE로 표시됐다.

Docker Desktop을 시작하고 다음을 확인했다.

```text
Docker Engine: 29.4.1
coderunner image: dongjun-coderunner:latest
divide_and_conquer-2448 cpp AC 6/6
```

이는 케이스나 reference 코드 오류가 아니라 Docker 엔진 미실행으로 발생한 환경 오류였다.

## 검증 결과

```text
python scripts/verify-judge-overrides.py divide_and_conquer-2448 ... dynamic_programming_1-15624
OK: 20 override files self-judged successfully.
```

```text
python -m unittest harness.tests.test_judge
Ran 9 tests in 2.564s
OK
```

```text
npm.cmd run judge:quality
total: 1009
averageQualityScore: 80.34
lowQualityCount: 392
missingStressCount: 0
allHaveOverride: true
```

```text
python -m py_compile <batch 10 override files>
OK
```

## 남은 작업

- 일반 override의 실제 6개 미만 수는 `412 -> 392`로 감소했다.
- 품질 감사의 낮은 품질 카운트는 `411 -> 392`로 감소했다.
- `divide_and_conquer-2448`은 기존 점수상 낮은 품질 집계 대상이 아니었기 때문에 두 감소량에 1개 차이가 있다.
- 다음 배치는 `dynamic_programming_1-1577`부터 이어서 처리한다.
