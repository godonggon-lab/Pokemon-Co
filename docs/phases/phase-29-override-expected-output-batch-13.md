# Phase 29 - Override Expected Output Batch 13

## 목표

남은 `disjoint_set` 문제를 마무리하고, `divide_and_conquer` 및 `dynamic_programming_1` 초반 문제에 expected output을 추가한다. 이 배치에는 special judge가 있는 타일링/패턴 문제도 포함되어 있어, 유효한 expected를 생성하면서 기존 checker 구조를 유지했다.

## 처리한 문제

- `disjoint_set-20955`
- `disjoint_set-3108`
- `disjoint_set-7511`
- `divide_and_conquer-1030`
- `divide_and_conquer-14600`
- `divide_and_conquer-14601`
- `divide_and_conquer-1493`
- `divide_and_conquer-16438`
- `divide_and_conquer-1780`
- `divide_and_conquer-1802`
- `divide_and_conquer-2374`
- `divide_and_conquer-5904`
- `dynamic_programming_1-1003`
- `dynamic_programming_1-1010`
- `dynamic_programming_1-10211`
- `dynamic_programming_1-10844`
- `dynamic_programming_1-11051`
- `dynamic_programming_1-11052`
- `dynamic_programming_1-11057`
- `dynamic_programming_1-11060`

## 구현 내용

- 트리 연결/사이클 수, 직사각형 연결 그룹, 네트워크 연결 시나리오 문제에 expected 생성기를 추가했다.
- 프랙탈 평면, 트로미노 타일링, 큐브 채우기, AB 7줄 패턴, 종이의 개수, 종이 접기, 수열 증가 비용, Moo 수열 문제에 expected 생성기를 추가했다.
- 피보나치 호출 횟수, 다리 놓기 조합, 최대 부분 배열, 쉬운 계단 수, 이항 계수, 카드 구매, 오르막 수, 점프 최소 횟수 DP 문제에 expected 생성기를 추가했다.
- `divide_and_conquer-14600`, `divide_and_conquer-14601`, `divide_and_conquer-16438`은 여러 정답이 가능한 문제라 기존 `check_output`을 유지했다. expected는 유효한 한 가지 출력 예시로 생성된다.
- expected가 채워진 문제를 oracle failure 테스트 fixture로 계속 사용할 수 없어, 해당 테스트 fixture를 다음 누락 문제인 `dynamic_programming_1-13910`으로 이동했다.

## 검증 결과

실행한 명령:

```bash
python scripts/verify-judge-overrides.py disjoint_set-20955 disjoint_set-3108 disjoint_set-7511 divide_and_conquer-1030 divide_and_conquer-14600 divide_and_conquer-14601 divide_and_conquer-1493 divide_and_conquer-16438 divide_and_conquer-1780 divide_and_conquer-1802 divide_and_conquer-2374 divide_and_conquer-5904 dynamic_programming_1-1003 dynamic_programming_1-1010 dynamic_programming_1-10211 dynamic_programming_1-10844 dynamic_programming_1-11051 dynamic_programming_1-11052 dynamic_programming_1-11057 dynamic_programming_1-11060
npm run harness:test
npm run judge:quality
```

결과:

- 타깃 override 20개 모두 self-judge `AC`
- `npm run harness:test`: 20개 테스트 통과
- `npm run judge:quality`: 평균 품질 점수 `66.31`
- expected 누락 현황: `458`문제 / `1827`케이스

## 다음 단계

다음 배치는 `dynamic_programming_1-1149`부터 이어서 DP 기본 문제 expected를 채운다.
