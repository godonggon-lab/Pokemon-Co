# Phase 24 - Override Expected Output Batch 08

## 목표

`brute_force` 계열 override 20개에 expected output을 추가했다. 이번 배치는 완전탐색, 조합, DFS, 간단 수식, 확률 계산이 섞여 있어 기존 정답 코드의 출력 형식을 그대로 맞추는 데 집중했다.

## 처리한 문제

- `brute_force-1145`
- `brute_force-11502`
- `brute_force-1251`
- `brute_force-1254`
- `brute_force-12919`
- `brute_force-13410`
- `brute_force-1359`
- `brute_force-1411`
- `brute_force-1421`
- `brute_force-14225`
- `brute_force-1436`
- `brute_force-14391`
- `brute_force-14500`
- `brute_force-14501`
- `brute_force-14620`
- `brute_force-1487`
- `brute_force-14912`
- `brute_force-1503`
- `brute_force-1527`
- `brute_force-15270`

## 구현 내용

- 각 override에 deterministic `_solve` 함수를 추가했다.
- `brute_force-11502`는 소수 sieve를 미리 구성해 골드바흐 세 소수 출력을 기존 순서대로 만들었다.
- `brute_force-10472` 이전 배치와 같은 방식으로, 이번 배치의 완전탐색 문제들도 case 크기 안에서 직접 계산되도록 했다.
- `brute_force-14500`은 DFS와 T자 모양 별도 계산을 함께 사용해 테트로미노 최댓값을 구했다.
- `brute_force-14620`은 꽃 세 개의 중심 조합을 순회하며 겹침 여부와 비용을 계산했다.

## 검증 결과

### Targeted override verification

```powershell
python scripts/verify-judge-overrides.py brute_force-1145 brute_force-11502 brute_force-1251 brute_force-1254 brute_force-12919 brute_force-13410 brute_force-1359 brute_force-1411 brute_force-1421 brute_force-14225 brute_force-1436 brute_force-14391 brute_force-14500 brute_force-14501 brute_force-14620 brute_force-1487 brute_force-14912 brute_force-1503 brute_force-1527 brute_force-15270
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
- 평균 품질 점수: 64.33
- stress case 누락 수: 0
- override 누락 수: 0

## Expected output 누락 감소

이번 배치 전:

- expected 누락 문제 수: 578
- expected 누락 case 수: 2346

이번 배치 후:

- expected 누락 문제 수: 558
- expected 누락 case 수: 2253

감소량:

- 문제 20개 개선
- case 93개 개선

## 다음 단계

- `brute_force` 계열 expected output 보강을 이어서 진행한다.
- expected 보강이 끝난 뒤에도 case 수가 부족한 문제는 별도 edge/fuzz 확장 배치에서 처리한다.
