# Phase 75 - 저빈도 케이스 보강 배치 22

## 목표

`simulation-17135`부터 `simulation-2933`까지
시뮬레이션 override 20개의 입력 케이스를 최소 6개로 보강한다.

## 처리한 문제

- `simulation-17135`
- `simulation-17140`
- `simulation-17143`
- `simulation-17779`
- `simulation-17780`
- `simulation-17822`
- `simulation-17837`
- `simulation-18500`
- `simulation-18809`
- `simulation-19235`
- `simulation-19236`
- `simulation-19237`
- `simulation-19238`
- `simulation-20055`
- `simulation-20056`
- `simulation-20665`
- `simulation-21609`
- `simulation-21922`
- `simulation-22861`
- `simulation-2933`

## 구현 내용

- 성 방어와 낚시왕 문제에 빈 보드, 단일 대상, 같은 칸 충돌 케이스를 추가했다.
- 배열 연산과 원판 회전 문제에 즉시 종료, 전체 삭제, 평균 조정 케이스를 추가했다.
- 윷놀이와 상어 시뮬레이션에 단일 객체, 경계 반전, 즉시 종료 케이스를 추가했다.
- 미네랄 문제에 빈 동굴, 단일 미네랄, 바닥에 연결된 군집을 추가했다.
- 모노미노도미노와 컨베이어 벨트 문제에 블록 방향별 입력과 최소 내구도 조건을 추가했다.
- 택시, 스터디 카페, 블록 그룹, 에어컨 문제에 연료 부족, 좌석 점유, 그룹 부재와 반사 규칙을 추가했다.
- 폴더 문제에 중복 파일명과 깊은 단일 경로를 추가했다.

## 발견하고 수정한 oracle 결함

`simulation-19235`의 파란 보드 좌표 변환에서 가로 블록과 세로 블록의 회전 좌표가 잘못되어 있었다.

- 가로 블록은 회전 후 세로 블록이 되며 열은 `3 - x`를 사용한다.
- 세로 블록은 회전 후 가로 블록이 되며 시작 열은 `2 - x`를 사용한다.
- 기존 구현은 `x=0`인 유효한 세로 블록에서 배열 범위를 벗어날 수 있었다.
- 변환식을 수정하고 기존 edge 및 stress 기대값도 올바른 결과로 교정했다.

## 검증 결과

```text
override self-judge: 20개 모두 AC (각 6/6)
unittest: 9 tests OK
JSON parse: OK
py_compile: OK
```

```text
total: 1009
averageQualityScore: 86.29
lowQualityCount: 152
missingStressCount: 0
allHaveOverride: true
```

## 작업 결과

- 저품질 override 수가 `172 -> 152`로 감소했다.
- 평균 품질 점수가 `85.79 -> 86.29`로 상승했다.
- 다음 일반 배치는 `simulation-8972`부터 진행한다.
