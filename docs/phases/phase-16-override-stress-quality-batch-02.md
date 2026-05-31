# Phase 16. Override Stress Quality Batch 02

## 목표

남아 있던 `stressCount == 0` override를 모두 제거한다. Phase 15 이후 남은 문제는 구현, 문자열, 시뮬레이션, 수학, 출력 전용 완전탐색 문제가 중심이었다.

## 작업 내용

- 28개 override에 stress case를 추가했다.
- `brute_force-4690`처럼 출력만 있는 문제는 `stress("", expected)`로 관리하도록 정리했다.
- 기존에 선언만 되어 있던 `REPLACE_SAMPLES=True`를 `harness/judge_core.py`가 실제로 반영하도록 수정했다.
  - 이 플래그가 있는 문제는 BOJ sample을 섞지 않고 override case만 채점한다.
  - 출력 전용 문제나 별도 override가 sample을 대체해야 하는 문제에서 오탐을 막는다.

## Stress 보강 문제

- `brute_force-4690`
- `implementation-1283`
- `implementation-16719`
- `implementation-17276`
- `implementation-17406`
- `implementation-17470`
- `implementation-18311`
- `implementation-20164`
- `implementation-20327`
- `implementation-21277`
- `implementation-21611`
- `implementation-22858`
- `implementation-22859`
- `implementation-22860`
- `implementation-2469`
- `implementation-9934`
- `math-1669`
- `simulation-3025`
- `string-19844`
- `string-19948`
- `string-20114`
- `string-20210`
- `string-2115`
- `string-3005`
- `string-3107`
- `string-4446`
- `string-4836`
- `string-9242`

## 실행 결과

```bash
npm run judge:quality
```

- `total`: 1009
- `averageQualityScore`: 61.35
- `missingStressCount`: 0
- `allHaveOverride`: true

```bash
python scripts/verify-judge-overrides.py brute_force-4690 implementation-1283 implementation-16719 implementation-17276 implementation-17406 implementation-17470 implementation-18311 implementation-20164 implementation-20327 implementation-21277 implementation-21611 implementation-22858 implementation-22859 implementation-22860 implementation-2469 implementation-9934 simulation-3025 string-19844 string-19948 string-20114 string-20210 string-2115 string-3005 string-3107 string-4446 string-4836 string-9242 math-1669
```

- 28개 수정 override 모두 `AC`

```bash
npm run harness:test
```

- 19개 테스트 통과

## 남은 일

- 이제 모든 override에 stress case는 존재한다.
- 다음 품질 과제는 `some_cases_need_oracle`을 줄이는 것이다.
  - 가능한 문제부터 expected output을 override 내부 `_solve`로 고정한다.
  - oracle 실행 의존도를 줄이면 CI와 운영 채점의 흔들림이 줄어든다.
