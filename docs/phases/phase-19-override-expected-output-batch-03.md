# Phase 19 - Override Expected Output Batch 03

## 목표

Backtracking override의 expected output 누락을 추가로 줄였다. 이번 배치도 문제별 입력 생성은 유지하고, 각 case에 대해 deterministic expected output을 생성하는 `_solve` 함수를 추가하는 방식으로 진행했다.

## 처리한 문제

- `backtracking-15664`
- `backtracking-15665`
- `backtracking-15666`
- `backtracking-15684`
- `backtracking-15918`
- `backtracking-16198`
- `backtracking-16571`
- `backtracking-16922`
- `backtracking-16938`
- `backtracking-16987`
- `backtracking-17136`
- `backtracking-1729`
- `backtracking-1759`
- `backtracking-1799`
- `backtracking-18290`
- `backtracking-18429`
- `backtracking-1941`
- `backtracking-19699`
- `backtracking-1987`
- `backtracking-19942`

## 구현 내용

- 순열/조합 계열 문제는 `itertools` 기반으로 expected output을 생성했다.
- 사다리 조작, 색종이 붙이기, 비숍, 칠공주, 알파 틱택토처럼 상태 탐색이 필요한 문제는 override 내부에 작은 완전탐색 solver를 추가했다.
- 모든 solver는 override의 기존 case 크기에 맞춰 빠르게 실행되도록 작성했다.
- 사용자 제출 언어와 무관하게 같은 input/output 기준으로 채점되도록 case마다 `expected` 문자열을 고정했다.

## 검증 결과

### Targeted override verification

```powershell
python scripts/verify-judge-overrides.py backtracking-15664 backtracking-15665 backtracking-15666 backtracking-15684 backtracking-15918 backtracking-16198 backtracking-16571 backtracking-16922 backtracking-16938 backtracking-16987 backtracking-17136 backtracking-1729 backtracking-1759 backtracking-1799 backtracking-18290 backtracking-18429 backtracking-1941 backtracking-19699 backtracking-1987 backtracking-19942
```

결과:

- 20개 override 모두 `AC`
- `OK: 20 override files self-judged successfully.`

### Harness test

```powershell
npm run harness:test
```

결과:

- 20개 테스트 통과
- 실패 없음

### Judge quality

```powershell
npm run judge:quality
```

결과:

- 전체 문제 수: 1009
- 평균 품질 점수: 62.34
- stress case 누락 수: 0
- override 누락 수: 0

## Expected output 누락 감소

이번 배치 전:

- expected 누락 문제 수: 678
- expected 누락 case 수: 2708

이번 배치 후:

- expected 누락 문제 수: 658
- expected 누락 case 수: 2634

감소량:

- 문제 20개 개선
- case 74개 개선

## 다음 단계

- 다음 20개 배치도 expected output 누락 문제를 우선 처리한다.
- backtracking 잔여분을 먼저 마무리하고, 이후 `binary_search` 계열로 넘어가는 흐름이 좋다.
- case 수가 2-3개뿐인 문제는 expected 추가 후에도 `case_count_lt_6` 경고가 남으므로, 별도 배치에서 edge/fuzz case 확장을 진행한다.
