# Phase 23 - Override Expected Output Batch 07

## 목표

`binary_search` 잔여 문제 12개와 `brute_force` 초입 문제 8개에 expected output을 추가했다. 이번 배치로 binary search 계열의 expected output 보강은 대부분 마무리 단계에 들어갔다.

## 처리한 문제

- `binary_search-2613`
- `binary_search-2776`
- `binary_search-2792`
- `binary_search-2805`
- `binary_search-2866`
- `binary_search-3020`
- `binary_search-3079`
- `binary_search-6209`
- `binary_search-6236`
- `binary_search-7795`
- `binary_search-8983`
- `binary_search-9007`
- `brute_force-1018`
- `brute_force-1025`
- `brute_force-10448`
- `brute_force-10472`
- `brute_force-1059`
- `brute_force-1065`
- `brute_force-11170`
- `brute_force-1120`

## 구현 내용

- 각 override에 deterministic `_solve` 함수를 추가했다.
- `binary_search-2613`은 최대 그룹 합과 그룹 크기 출력까지 기존 정답과 같은 방식으로 생성했다.
- `binary_search-3020`, `binary_search-7795`, `binary_search-8983`은 `bisect` 기반 expected를 추가했다.
- `binary_search-9007`은 두 배열 합을 만든 뒤 target과 가장 가까운 합을 tie-break까지 맞춰 계산했다.
- `brute_force-10472`는 3x3 버튼 상태 전체 BFS를 미리 계산한 뒤 case별 expected를 생성했다.

## 검증 결과

### Targeted override verification

```powershell
python scripts/verify-judge-overrides.py binary_search-2613 binary_search-2776 binary_search-2792 binary_search-2805 binary_search-2866 binary_search-3020 binary_search-3079 binary_search-6209 binary_search-6236 binary_search-7795 binary_search-8983 binary_search-9007 brute_force-1018 brute_force-1025 brute_force-10448 brute_force-10472 brute_force-1059 brute_force-1065 brute_force-11170 brute_force-1120
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
- 평균 품질 점수: 63.93
- stress case 누락 수: 0
- override 누락 수: 0

## Expected output 누락 감소

이번 배치 전:

- expected 누락 문제 수: 598
- expected 누락 case 수: 2428

이번 배치 후:

- expected 누락 문제 수: 578
- expected 누락 case 수: 2346

감소량:

- 문제 20개 개선
- case 82개 개선

## 다음 단계

- `brute_force` 계열 expected output 보강을 이어서 진행한다.
- case 수가 적어 품질 점수가 낮게 남는 문제는 expected 보강 이후 별도 edge/fuzz 확장 배치에서 처리한다.
