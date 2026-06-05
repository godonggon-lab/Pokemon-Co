# Phase 30 - Override Expected Output Batch 14

## 목표

`dynamic_programming_1` 기본 문제 20개에 expected output을 추가한다. 이번 배치는 RGB 거리, LIS/LDS, 타일링, 격자 DP, 지름길, 피보나치, 조합, 1/2/3 더하기 계열처럼 앱에서 자주 출제될 수 있는 기초 DP 문제를 oracle 없이 안정적으로 채점하는 데 초점을 맞췄다.

## 처리한 문제

- `dynamic_programming_1-1149`
- `dynamic_programming_1-11568`
- `dynamic_programming_1-11722`
- `dynamic_programming_1-11726`
- `dynamic_programming_1-11727`
- `dynamic_programming_1-1309`
- `dynamic_programming_1-13699`
- `dynamic_programming_1-13910`
- `dynamic_programming_1-14430`
- `dynamic_programming_1-1446`
- `dynamic_programming_1-14852`
- `dynamic_programming_1-1495`
- `dynamic_programming_1-1535`
- `dynamic_programming_1-15489`
- `dynamic_programming_1-15624`
- `dynamic_programming_1-1577`
- `dynamic_programming_1-15988`
- `dynamic_programming_1-15991`
- `dynamic_programming_1-15992`
- `dynamic_programming_1-15993`

## 구현 내용

- 각 override에 문제별 `_solve()`를 추가하고 기존 edge/stress 입력에 expected를 채웠다.
- 저장된 정답 코드의 점화식과 모듈러 기준을 그대로 맞췄다.
- `dynamic_programming_1-15988`, `15991`, `15992`, `15993`은 모두 `1,000,000,009` 모듈러 기준을 적용했다.
- expected가 채워진 문제를 oracle failure 테스트 fixture로 계속 사용할 수 없어서, fixture를 다음 누락 문제인 `dynamic_programming_1-16195`로 이동했다.

## 검증 결과

실행한 명령:

```bash
python scripts/verify-judge-overrides.py dynamic_programming_1-1149 dynamic_programming_1-11568 dynamic_programming_1-11722 dynamic_programming_1-11726 dynamic_programming_1-11727 dynamic_programming_1-1309 dynamic_programming_1-13699 dynamic_programming_1-13910 dynamic_programming_1-14430 dynamic_programming_1-1446 dynamic_programming_1-14852 dynamic_programming_1-1495 dynamic_programming_1-1535 dynamic_programming_1-15489 dynamic_programming_1-15624 dynamic_programming_1-1577 dynamic_programming_1-15988 dynamic_programming_1-15991 dynamic_programming_1-15992 dynamic_programming_1-15993
npm run harness:test
npm run judge:quality
```

결과:

- 타깃 override 20개 모두 self-judge `AC`
- `npm run harness:test`: 통과
- Docker daemon이 꺼진 상태라 Docker 전용 테스트 5개는 skip
- `npm run judge:quality`: 평균 품질 점수 `66.70`
- expected 누락 현황: `438`문제 / `1748`케이스

## 다음 단계

다음 배치는 `dynamic_programming_1-16194`부터 이어서 DP1 나머지 문제를 처리한다.
