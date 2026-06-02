# Phase 28 - Override Expected Output Batch 12

## 목표

`data_structure2`와 `disjoint_set` 계열 override 20개에 expected output을 추가한다. 이 배치의 핵심은 해시/힙/우선순위큐 문제와 유니온파인드 기반 문제를 oracle 없이도 안정적으로 채점할 수 있게 만드는 것이다.

## 처리한 문제

- `data_structure2-10546`
- `data_structure2-1269`
- `data_structure2-12764`
- `data_structure2-1302`
- `data_structure2-1655`
- `data_structure2-17255`
- `data_structure2-21942`
- `data_structure2-9375`
- `disjoint_set-10775`
- `disjoint_set-11085`
- `disjoint_set-12893`
- `disjoint_set-14595`
- `disjoint_set-15789`
- `disjoint_set-16168`
- `disjoint_set-16724`
- `disjoint_set-17090`
- `disjoint_set-1717`
- `disjoint_set-17398`
- `disjoint_set-1976`
- `disjoint_set-20040`

## 구현 내용

- 완주하지 못한 선수, 대칭 차집합, 컴퓨터실 자리 배정, 베스트셀러, 가운데를 말해요, 문자열 확장 경로 수, 부품 대여장, 패션 조합 문제에 expected 생성기를 추가했다.
- 공항 도킹, 너비 우선 최대 경로, 이분 그래프 판정, 방 벽 제거, 왕국 병합, 오일러 경로 가능성, safe zone, 탈출 가능 칸, 집합 표현, 간선 제거 역순 비용, 여행 계획, 사이클 게임 문제에 expected 생성기를 추가했다.
- `disjoint_set-16724`는 기존 override에 문제 조건 밖 입력이 포함되어 있어, 저장된 Python 정답 코드의 인덱싱 동작을 기준으로 expected를 맞췄다.
- expected가 채워진 문제를 oracle failure 테스트 fixture로 계속 사용할 수 없어서, fixture를 다음 expected 누락 문제인 `disjoint_set-20955`의 실제 정답 코드로 옮겼다.

## 검증 결과

실행한 명령:

```bash
python scripts/verify-judge-overrides.py data_structure2-10546 data_structure2-1269 data_structure2-12764 data_structure2-1302 data_structure2-1655 data_structure2-17255 data_structure2-21942 data_structure2-9375 disjoint_set-10775 disjoint_set-11085 disjoint_set-12893 disjoint_set-14595 disjoint_set-15789 disjoint_set-16168 disjoint_set-16724 disjoint_set-17090 disjoint_set-1717 disjoint_set-17398 disjoint_set-1976 disjoint_set-20040
npm run harness:test
npm run judge:quality
```

결과:

- 타깃 override 20개 모두 self-judge `AC`
- `npm run harness:test`: 20개 테스트 통과
- `npm run judge:quality`: 평균 품질 점수 `65.91`
- expected 누락 현황: `478`문제 / `1905`케이스

## 다음 단계

다음 배치는 `disjoint_set-20955`, `disjoint_set-3108`, `disjoint_set-7511`을 마저 처리하고 `divide_and_conquer` 계열로 넘어간다.
