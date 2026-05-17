# Phase 13 First 5. 첫 편입 검토 문제

## 목표

외부 풀이가 있고 statement/sample 확보가 된 쉬운 문제 5개를 골라 실제 편입 검토를 시작한다.

## 선정 기준

- Python 또는 C++ 정답 코드가 있다.
- Wayback 기반 statement/sample 확보가 됐다.
- 문제 유형이 비교적 명확해서 edge/fuzz case를 작성하기 쉽다.

## 후보

| BOJ | 제목 | slug | 언어 | sample | 상태 |
|---|---|---|---|---:|---|
| 4949 | 균형잡힌 세상 | data_structure-4949 | cpp | 1 | statement 확보 |
| 11256 | 사탕 | greedy-11256 | python | 2 | statement 확보 |
| 11441 | 합 구하기 | prefix_sum-11441 | cpp, java, python | 2 | statement 확보 |
| 1697 | 숨바꼭질 | graph_traversal-1697 | python | 1 | statement 확보 |
| 2156 | 포도주 시식 | dynamic_programming_1-2156 | cpp, java, python | 1 | statement 확보 |

## 다음 작업

1. 각 문제의 BOJ 원문을 그대로 복제하지 않고 앱용 요약을 작성한다.
2. 외부 정답 코드를 로컬 oracle 후보로 저장할지, 직접 oracle을 새로 작성할지 결정한다.
3. sample case를 먼저 통과시킨다.
4. edge/fuzz case를 작성한다.
5. 5개 모두 통과하면 `data/problems.json` 편입 방식을 확정한다.

## 실행 결과

- 생성 시각: 2026-05-13T15:20:22.895Z
- 출력: `data/problem-expansion-first-5.json`

## 2026-05-14 편입 실행 결과

명령:

```bash
npm run problems:import-first-5
npm run data:map
npx next build
```

결과:

- `data/problems-extra.json`에 첫 5문제를 추가했다.
- 앱 데이터 로더가 `data/problems.json`과 `data/problems-extra.json`을 함께 읽도록 변경했다.
- 포켓몬 매핑 스크립트가 확장 문제도 포함하도록 변경했다.
- `monster-map` 매핑 수가 362개에서 367개로 늘었다.
- Next.js build가 통과했고, 문제 상세 정적 페이지가 367개 문제 기준으로 생성됐다.

편입된 문제:

| BOJ | 제목 | slug | 언어 |
|---|---|---|---|
| 4949 | 균형잡힌 세상 | data_structure-4949 | cpp |
| 11256 | 사탕 | greedy-11256 | python |
| 11441 | 합 구하기 | prefix_sum-11441 | python, cpp |
| 1697 | 숨바꼭질 | graph_traversal-1697 | python |
| 2156 | 포도주 시식 | dynamic_programming_1-2156 | python, cpp |

주의:

- 아직 이 5문제는 sample 기반 statement와 정답 코드 연결까지 완료된 상태다.
- 문제별 edge/fuzz override는 다음 단계에서 작성해야 한다.

## 2026-05-14 override 보강 결과

추가한 override:

- `harness/overrides/data_structure-4949.py`
- `harness/overrides/greedy-11256.py`
- `harness/overrides/prefix_sum-11441.py`
- `harness/overrides/graph_traversal-1697.py`
- `harness/overrides/dynamic_programming_1-2156.py`

검증 명령:

```bash
python scripts/verify-judge-overrides.py data_structure-4949 greedy-11256 prefix_sum-11441 graph_traversal-1697 dynamic_programming_1-2156
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

검증 결과:

- 첫 5문제 override self-judge: 모두 AC
- judge coverage: 367개 전부 judge ready
- missing case: 0개
- 확장 문제 포함 언어 감사 통과
- Next.js build 통과

수정 사항:

- `scripts/verify-judge-overrides.py`가 `data/problems-extra.json`도 읽도록 변경했다.
- `scripts/audit-judge-cases.mjs`, `scripts/audit-judge-coverage.mjs`, `scripts/audit-language-support.mjs`, `scripts/fetch-solvedac.mjs`가 확장 문제도 포함하도록 변경했다.
- `data_structure-4949`는 외부 C++ 소스만 있으면 Docker 미실행 로컬 검증이 불편하므로, 안정적인 Python 소스를 함께 추가했다.
