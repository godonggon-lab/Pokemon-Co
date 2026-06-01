# Phase 20 - Override Expected Output Batch 04

## 목표

Backtracking 잔여 override와 binary search 초입 문제에 expected output을 추가했다. 이번 배치에서는 스도쿠처럼 기존 stress case 자체가 잘못된 문제도 발견해, solvable input으로 수정했다.

## 처리한 문제

- `backtracking-19949`
- `backtracking-20208`
- `backtracking-2023`
- `backtracking-2026`
- `backtracking-20950`
- `backtracking-2239`
- `backtracking-22944`
- `backtracking-2529`
- `backtracking-2661`
- `backtracking-2922`
- `backtracking-3165`
- `backtracking-3980`
- `backtracking-6443`
- `backtracking-6603`
- `backtracking-6987`
- `backtracking-7490`
- `backtracking-7682`
- `backtracking-9944`
- `binary_search-1072`
- `binary_search-10816`

## 구현 내용

- 각 override에 deterministic `_solve` 함수를 추가했다.
- 스도쿠 문제 `backtracking-2239`는 기존 stress 입력이 해가 없는 형태라서, 해가 존재하는 입력으로 교체했다.
- 여러 정답 후보를 출력하는 문제는 기존 백준 정답 코드와 같은 순서로 출력되도록 구성했다.
- `binary_search-1072`, `binary_search-10816`은 각각 이분 탐색/카운팅 기준으로 expected output을 생성했다.

## 검증 결과

### Targeted override verification

```powershell
python scripts/verify-judge-overrides.py backtracking-19949 backtracking-20208 backtracking-2023 backtracking-2026 backtracking-20950 backtracking-2239 backtracking-22944 backtracking-2529 backtracking-2661 backtracking-2922 backtracking-3165 backtracking-3980 backtracking-6443 backtracking-6603 backtracking-6987 backtracking-7490 backtracking-7682 backtracking-9944 binary_search-1072 binary_search-10816
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
- 평균 품질 점수: 62.74
- stress case 누락 수: 0
- override 누락 수: 0

## Expected output 누락 감소

이번 배치 전:

- expected 누락 문제 수: 658
- expected 누락 case 수: 2634

이번 배치 후:

- expected 누락 문제 수: 638
- expected 누락 case 수: 2566

감소량:

- 문제 20개 개선
- case 68개 개선

## 다음 단계

- 다음 배치부터는 `binary_search` 계열 expected output 보강을 본격적으로 진행한다.
- expected output 추가 후에도 case 수가 부족한 문제는 별도 품질 강화 배치에서 edge/fuzz case를 늘린다.
