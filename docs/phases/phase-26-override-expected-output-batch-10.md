# Phase 26 - Override Expected Output Batch 10

## 목표

브루트포스 override 20개에 expected output을 추가해서 oracle 의존 케이스를 줄이고, Python/C++ 제출이 동일한 입력/출력 기준으로 채점되도록 강화한다.

이번 배치는 `brute_force-17610`부터 `brute_force-3040`까지 처리했다. `brute_force-2798`은 이미 일부 expected가 있었지만 fuzz 케이스 2개가 oracle 의존 상태였기 때문에 함께 보강했다.

## 처리한 문제

- `brute_force-17610`
- `brute_force-17626`
- `brute_force-18511`
- `brute_force-18512`
- `brute_force-18808`
- `brute_force-18868`
- `brute_force-1895`
- `brute_force-1969`
- `brute_force-19947`
- `brute_force-21278`
- `brute_force-21315`
- `brute_force-2160`
- `brute_force-21943`
- `brute_force-2304`
- `brute_force-2435`
- `brute_force-2503`
- `brute_force-2635`
- `brute_force-2798`
- `brute_force-2961`
- `brute_force-3040`

## 구현 내용

- 양팔저울, 사수 합, K-진수 후보 탐색, 두 등차 위치 교차, 스티커 붙이기, 우주신과의 교감형 순위 비교, 3x3 중앙값 필터, DNA consensus, 투자 DP, 치킨집 거리, 카드 섞기, 그림 비교, 연산 그룹 분할, 창고 다각형, 연속 온도 합, 숫자야구, 수 이어가기, 블랙잭, 신맛/쓴맛 부분집합, 일곱 난쟁이에 expected 생성기를 추가했다.
- `brute_force-21315`와 `brute_force-18808`은 저장된 정답 코드의 세부 동작을 기준으로 구현했다.
- `brute_force-2798`의 fuzz expected가 채워지면서 oracle 실패 테스트가 더 이상 이 문제에 의존할 수 없게 되어, `harness/tests/test_judge.py`의 oracle 실패 fixture를 `brute_force-3085`로 옮겼다.

## 검증 결과

실행한 명령:

```bash
python scripts/verify-judge-overrides.py brute_force-17610 brute_force-17626 brute_force-18511 brute_force-18512 brute_force-18808 brute_force-18868 brute_force-1895 brute_force-1969 brute_force-19947 brute_force-21278 brute_force-21315 brute_force-2160 brute_force-21943 brute_force-2304 brute_force-2435 brute_force-2503 brute_force-2635 brute_force-2798 brute_force-2961 brute_force-3040
npm run harness:test
npm run judge:quality
```

결과:

- 타깃 override 20개 모두 self-judge `AC`
- `npm run harness:test`: 20개 테스트 통과
- `npm run judge:quality`: 평균 품질 점수 `65.12`
- expected 누락 현황: `518`문제 / `2095`케이스

## 다음 단계

다음 배치는 `brute_force-3085`부터 이어서 처리한다. 브루트포스 묶음이 끝나면 `data_structure` 계열부터 같은 방식으로 expected output을 채워간다.
