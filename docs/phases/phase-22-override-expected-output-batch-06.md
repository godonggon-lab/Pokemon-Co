# Phase 22 - Override Expected Output Batch 06

## 목표

`binary_search` 계열 override 20개에 expected output을 추가했다. 이번 배치는 이분 탐색뿐 아니라 BFS, two-pointer, 근접값 탐색, 실수 이분 탐색이 섞여 있어 기존 정답 코드의 출력 규칙과 tie-break를 그대로 맞추는 데 집중했다.

## 처리한 문제

- `binary_search-17179`
- `binary_search-17266`
- `binary_search-17393`
- `binary_search-17451`
- `binary_search-17503`
- `binary_search-17951`
- `binary_search-18113`
- `binary_search-18114`
- `binary_search-1939`
- `binary_search-2022`
- `binary_search-20495`
- `binary_search-20551`
- `binary_search-2121`
- `binary_search-22871`
- `binary_search-22945`
- `binary_search-2343`
- `binary_search-2412`
- `binary_search-2467`
- `binary_search-2470`
- `binary_search-2512`

## 구현 내용

- 각 override에 deterministic `_solve` 함수를 추가했다.
- `binary_search-2022`는 기존 풀이처럼 100회 반복 후 소수점 셋째 자리까지 출력하도록 맞췄다.
- `binary_search-2412`는 기존 BFS 도달 판정을 그대로 재현했다.
- `binary_search-2467`, `binary_search-2470`은 용액 두 개의 출력 순서가 기존 정답과 일치하도록 정렬/two-pointer 기준을 맞췄다.
- `binary_search-20495`, `binary_search-20551`은 `bisect` 기반으로 expected output을 생성했다.

## 검증 결과

### Targeted override verification

```powershell
python scripts/verify-judge-overrides.py binary_search-17179 binary_search-17266 binary_search-17393 binary_search-17451 binary_search-17503 binary_search-17951 binary_search-18113 binary_search-18114 binary_search-1939 binary_search-2022 binary_search-20495 binary_search-20551 binary_search-2121 binary_search-22871 binary_search-22945 binary_search-2343 binary_search-2412 binary_search-2467 binary_search-2470 binary_search-2512
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
- 평균 품질 점수: 63.53
- stress case 누락 수: 0
- override 누락 수: 0

## Expected output 누락 감소

이번 배치 전:

- expected 누락 문제 수: 618
- expected 누락 case 수: 2495

이번 배치 후:

- expected 누락 문제 수: 598
- expected 누락 case 수: 2428

감소량:

- 문제 20개 개선
- case 67개 개선

## 다음 단계

- 남은 `binary_search` 문제 6개를 처리한 뒤, `brute_force` 계열 expected output 보강으로 넘어간다.
- expected output이 채워진 뒤에도 case 수가 부족한 문제는 별도 batch에서 edge/fuzz case를 확장한다.
