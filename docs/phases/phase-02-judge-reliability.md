# Phase 02. 채점 신뢰도 개선

## 목표

현재 채점은 카테고리 기반 fuzz input과 oracle 출력 비교에 의존합니다. 실제 BOJ 문제별 입력 형식과 어긋날 수 있으므로 sample/custom/fuzz를 분리해 채점 신뢰도를 높입니다.

## 범위

- sample test 우선 실행 구조 설계
- `data/problems-statements.json`에서 sample input/output 사용 가능 여부 확인
- `CaseResult.kind`를 `sample`, `fuzz`로 구분
- generator/oracle 실패를 일반 WA와 분리
- 재현 가능한 seed와 실패 입력 기록
- 주요 문제부터 `harness/overrides` 추가

## 완료 기준

- sample이 있는 문제는 sample을 먼저 실행한다.
- fuzz 실패와 sample 실패가 결과 UI에서 구분된다.
- `npm run harness:test`가 통과한다.
- `npm run build`가 통과한다.

## 작업 로그

- `data/problems-statements.json` 구조를 확인했다.
- 2798 문제에 sample 2개가 들어 있음을 확인했다.
- `harness/judge_core.py`에 sample case loader를 추가했다.
- sample case는 statement의 expected output을 직접 사용하고, fuzz case는 기존처럼 oracle 실행 결과를 사용하도록 분리했다.
- `CaseResult.kind`에 `sample` 또는 `fuzz`가 들어가도록 수정했다.
- sample이 fuzz보다 먼저 실행되는지 검증하는 단위 테스트를 추가했다.
- `package.json`의 `harness:test`를 `pytest`가 아닌 표준 `unittest discover` 기반으로 변경했다.

## 실행 결과(Output)

### 1. statement sample 구조 확인

명령:

```bash
python - <<'PY'
import json
from pathlib import Path
s = json.loads(Path('data/problems-statements.json').read_text(encoding='utf-8'))
print(s['2798']['samples'][:2])
PY
```

결과 요약:

```text
2798 sample #1 input: 5 21 / 5 6 7 8 9
2798 sample #1 output: 21
2798 sample #2 output: 497
```

판단:

- 문제문 데이터에 sample input/output이 구조화되어 있다.
- 채점 전에 sample을 먼저 실행할 수 있다.

### 2. sample/fuzz 실행 순서 확인

명령:

```bash
python - <<'PY'
from harness.judge_core import judge, LocalRunner
from harness.tests.test_judge import ORACLE_2798
r = judge(
    problem_slug='brute_force-2798',
    category_slug='brute_force',
    user_lang='python',
    user_code=ORACLE_2798,
    oracle_lang='python',
    oracle_code=ORACLE_2798,
    user_runner=LocalRunner(),
    oracle_runner=LocalRunner(),
    case_count=2,
)
print(r['status'], r['passed'], r['total'])
print([c['kind'] for c in r['cases']])
PY
```

결과:

```text
AC 4 4
['sample', 'sample', 'fuzz', 'fuzz']
```

판단:

- sample 2개가 먼저 실행되고, 이후 fuzz 2개가 실행된다.
- sample expected output은 statement에서 직접 사용한다.

### 3. Oracle/generator 실패 처리 확인

변경 내용:

- fuzz case의 expected output을 만들기 위해 oracle을 실행하다가 실패하면 더 이상 조용히 스킵하지 않는다.
- generator가 예외를 던지면 `WA`가 아니라 `ERR`로 반환한다.
- 이미 실행된 케이스가 있다면 oracle 실패 응답에 `cases`를 포함해 어디까지 진행됐는지 볼 수 있게 했다.

추가 테스트:

```text
test_oracle_failure_returns_ERR
test_generator_failure_returns_ERR
```

판단:

- 채점 인프라 문제와 사용자 오답이 섞이지 않게 되었다.
- Phase 02의 “generator/oracle 실패를 ERR로 세분화” 리스크는 해소했다.

### 4. Harness 테스트

명령:

```bash
npm run harness:test
```

결과:

```text
Ran 5 tests in 2.208s
OK
```

판단:

- 기존 AC/WA 테스트가 유지된다.
- sample 우선 실행 테스트가 추가로 통과한다.
- oracle/generator 실패가 `ERR`로 반환되는 테스트가 통과한다.
- `pytest` 없이 기본 Python `unittest`로 실행된다.

### 5. Production build

명령:

```bash
npm run build
```

결과 요약:

```text
[index-boj] categories: 22, problems: 362
[monster-map] 362 mappings
✓ Compiled successfully
✓ Generating static pages (392/392)
```

판단:

- 채점 코어 변경 후에도 Next.js production build가 통과한다.

## 예상 리스크

### 해소/정책 결정 완료

- 모든 문제에 sample 데이터가 있는 것은 아닙니다.
  - 정책: sample이 없으면 정상적으로 fuzz만 실행합니다.
  - 이유: BOJ 문제문 수집 실패나 오래된 문제에서도 채점이 멈추지 않게 하기 위함입니다.
- 아직 `custom` case는 구현하지 않았습니다.
  - 정책: Phase 03의 “사용자 custom input 실행” 기능에서 다룹니다.
  - 이유: custom case는 채점 코어보다 플레이그라운드 UX/API 계약과 함께 설계하는 편이 자연스럽습니다.
- generator/oracle 실패가 WA처럼 보일 수 있었습니다.
  - 조치: `ERR`로 반환하도록 수정했습니다.
  - 검증: `test_oracle_failure_returns_ERR`, `test_generator_failure_returns_ERR` 통과.

Phase 02 기준으로 남은 차단 리스크는 없습니다.
