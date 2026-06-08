# Phase 53 - Sharded Judge Verification CI

## 목표

전체 override self-judge 검증이 1009개 문제를 한 번에 실행하면서 10분 제한을 넘는 문제를 해결한다.

Phase 52에서 모든 override의 `expected` 미완료는 제거했지만, `npm run judge:verify-overrides` 전체 실행은 로컬 10분 제한에서 타임아웃되었다. 따라서 전체 검증을 CI/nightly에서 shard 단위로 나눠 실행할 수 있게 만든다.

## 구현 내용

### `scripts/verify-judge-overrides.py`

기존 사용법은 유지했다.

```text
python scripts/verify-judge-overrides.py
python scripts/verify-judge-overrides.py two_pointer-1806
```

새 옵션을 추가했다.

```text
python scripts/verify-judge-overrides.py --shard 1/8
python scripts/verify-judge-overrides.py --shard 1/8 --list-only
```

- `--shard INDEX/TOTAL`
  - 정렬된 override 목록을 deterministic modulo 방식으로 나눈다.
  - 예: `1/8`은 8개 shard 중 첫 번째 몫만 검증한다.
- `--list-only`
  - 실제 judge 실행 없이 선택된 slug 목록만 출력한다.
  - CI matrix나 shard 분할 확인용이다.
- slug 직접 지정과 shard는 함께 사용할 수 있다.

### `.github/workflows/judge-docker-nightly.yml`

기존 nightly workflow를 두 job으로 분리했다.

1. `docker-runner-verdicts`
   - Docker runner 자체의 CE/TLE/MLE/OLE 판정 테스트를 실행한다.
2. `verify-overrides`
   - matrix shard 8개로 override self-judge를 분할 실행한다.
   - 각 shard는 다음 명령을 실행한다.

```text
python scripts/verify-judge-overrides.py --shard <shard>/8
```

## 검증 결과

스크립트 문법 검사:

```text
python -m py_compile scripts/verify-judge-overrides.py
```

shard 분할 확인:

```text
counts [127, 126, 126, 126, 126, 126, 126, 126]
total 1009 unique 1009
```

직접 slug 검증:

```text
two_pointer-1806 python AC 6/6
OK: 1 override files self-judged successfully.
```

## 기대 효과

- 전체 override self-judge가 한 job에서 타임아웃되는 문제를 줄인다.
- 어느 shard가 실패했는지 GitHub Actions에서 바로 확인할 수 있다.
- 이후 케이스 수를 더 늘려도 shard 수를 늘리는 방식으로 검증 시간을 관리할 수 있다.

## 다음 작업

다음 phase에서는 케이스 수가 적은 문제를 우선순위로 보강한다.

현재 quality 감사에서 남은 큰 gap은 다음이다.

```text
case_count_lt_6
```

즉, expected는 모두 채워졌지만 일부 문제는 케이스 수가 2~5개라 edge/stress 보강이 필요하다.
