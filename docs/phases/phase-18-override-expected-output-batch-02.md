# Phase 18 - Override Expected Output Batch 02

## 목표

Judge override의 fuzz/stress case가 모든 언어에서 같은 기준으로 채점될 수 있도록, backtracking 문제 20개의 case에 `expected` 출력을 추가했다.

이번 배치는 입력 생성 자체보다 "생성된 입력에 대한 정답 출력 고정"이 목적이다. Python/C++ 사용자 코드가 같은 입력을 받았을 때 동일한 expected output과 비교되도록 만드는 작업이다.

## 처리한 문제

- `backtracking-10421`
- `backtracking-1062`
- `backtracking-10971`
- `backtracking-1248`
- `backtracking-12908`
- `backtracking-13908`
- `backtracking-1469`
- `backtracking-14888`
- `backtracking-1553`
- `backtracking-15566`
- `backtracking-15649`
- `backtracking-15650`
- `backtracking-15651`
- `backtracking-15652`
- `backtracking-15654`
- `backtracking-15655`
- `backtracking-15656`
- `backtracking-15658`
- `backtracking-15659`
- `backtracking-15663`

## 구현 내용

- 각 override에 문제별 `_solve` 함수를 추가했다.
- `CASES`를 만들 때 `{**case, "expected": _solve(...)}` 형태로 expected output을 고정했다.
- `backtracking-15566`은 출력이 여러 개 가능한 checker 문제라서 `expected`는 빈 문자열로 두고, 기존 `check_output` 기반의 의미 검증을 유지했다.
- 순열/조합/중복 순열/중복 조합 계열은 `itertools`를 사용해 문제 정의와 같은 순서로 출력되도록 했다.
- 연산자 끼워넣기 계열은 백준 기준의 0 방향 정수 나눗셈을 직접 맞췄다.

## 검증 결과

### Targeted override verification

```powershell
python scripts/verify-judge-overrides.py backtracking-10421 backtracking-1062 backtracking-10971 backtracking-1248 backtracking-12908 backtracking-13908 backtracking-1469 backtracking-14888 backtracking-1553 backtracking-15566 backtracking-15649 backtracking-15650 backtracking-15651 backtracking-15652 backtracking-15654 backtracking-15655 backtracking-15656 backtracking-15658 backtracking-15659 backtracking-15663
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
- 평균 품질 점수: 61.95
- stress case 누락 수: 0
- override 누락 수: 0

## Expected output 누락 감소

이번 배치 전:

- expected 누락 문제 수: 698
- expected 누락 case 수: 2796

이번 배치 후:

- expected 누락 문제 수: 678
- expected 누락 case 수: 2708

감소량:

- 문제 20개 개선
- case 88개 개선

## 다음 단계

- 같은 방식으로 다음 20개 override 배치를 진행한다.
- 우선순위는 expected output이 없는 문제를 먼저 줄이는 것이다.
- checker 문제는 exact output 비교가 아니라 의미 검증을 유지하되, judge 품질 audit에서 expected 누락으로 오해되지 않도록 별도 표식을 검토한다.
