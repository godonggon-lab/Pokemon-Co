# Phase 21 - Override Expected Output Batch 05

## 목표

`binary_search` 계열 override 20개에 expected output을 추가했다. 이 배치는 정수 이분 탐색, 실수 이분 탐색, 정렬 기반 근접값 탐색, 카운팅 문제를 포함한다.

## 처리한 문제

- `binary_search-11561`
- `binary_search-1166`
- `binary_search-11687`
- `binary_search-12757`
- `binary_search-1300`
- `binary_search-13397`
- `binary_search-13702`
- `binary_search-14575`
- `binary_search-14627`
- `binary_search-1477`
- `binary_search-1561`
- `binary_search-15732`
- `binary_search-15810`
- `binary_search-15823`
- `binary_search-16401`
- `binary_search-16434`
- `binary_search-1654`
- `binary_search-16564`
- `binary_search-16960`
- `binary_search-17124`

## 구현 내용

- 각 override에 deterministic `_solve` 함수를 추가했다.
- 실수 이분 탐색 문제 `binary_search-1166`은 기존 정답 코드와 같은 100회 반복 방식으로 expected를 생성했다.
- `binary_search-12757`, `binary_search-17124`처럼 근접값을 찾는 문제는 `bisect` 기반으로 tie-break 규칙을 반영했다.
- `binary_search-1561`, `binary_search-16434`처럼 시뮬레이션과 이분 탐색이 섞인 문제는 기존 풀이 조건을 그대로 재현했다.

## 검증 결과

### Targeted override verification

```powershell
python scripts/verify-judge-overrides.py binary_search-11561 binary_search-1166 binary_search-11687 binary_search-12757 binary_search-1300 binary_search-13397 binary_search-13702 binary_search-14575 binary_search-14627 binary_search-1477 binary_search-1561 binary_search-15732 binary_search-15810 binary_search-15823 binary_search-16401 binary_search-16434 binary_search-1654 binary_search-16564 binary_search-16960 binary_search-17124
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
- 평균 품질 점수: 63.14
- stress case 누락 수: 0
- override 누락 수: 0

## Expected output 누락 감소

이번 배치 전:

- expected 누락 문제 수: 638
- expected 누락 case 수: 2566

이번 배치 후:

- expected 누락 문제 수: 618
- expected 누락 case 수: 2495

감소량:

- 문제 20개 개선
- case 71개 개선

## 다음 단계

- `binary_search` 잔여 expected output 누락 문제를 계속 처리한다.
- expected output 보강 후에도 case 수가 적은 문제는 별도 batch에서 edge/fuzz case를 늘린다.
