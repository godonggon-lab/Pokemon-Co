# Phase 13 Batch 27 - Mixed Judge Override 20개 추가

## 목표

남은 확장 후보 중 exact compare로 검증 가능한 문제 20개를 추가한다. 이번 배치부터 남은 후보 수는 실제 앱 문제 목록과 `data/problem-expansion-candidates.json`의 차집합으로 다시 계산했다.

## 이번 배치 추가 문제

- `tree-1240`
- `brute_force-1359`
- `shortest_path-1446`
- `dynamic_programming_2-1535`
- `dynamic_programming_2-1577`
- `brute_force-1581`
- `dynamic_programming_2-2411`
- `binary_search-2613`
- `backtracking-2922`
- `simulation-8972`
- `backtracking-9944`
- `shortest_path-11780`
- `graph_traversal-13913`
- `simulation-16939`
- `brute_force-16986`
- `simulation-18500`
- `simulation-18809`
- `tree-19581`
- `tree-19641`
- `simulation-22861`

## 작업 내용

- 각 문제의 `harness/overrides/*.py`에 edge/stress 입력을 추가했다.
- `scripts/import-expansion-manual-batch-35.mjs`로 20개 문제 metadata와 oracle 코드를 `data/problems-extra.json`에 반영했다.
- `brute_force-1359`는 입력 포맷을 `N M K` 세 값으로 바로잡았다.
- 경로 출력이 포함된 문제는 테스트 입력에서 최단 경로가 안정적으로 정해지도록 구성했다.

## 검증 결과

- `python scripts/verify-judge-overrides.py ...20개 slug...`: 통과
- `npm run data:map`: 통과, monster mapping 977개
- `npm run judge:coverage`: 통과, judgeReady 977개, missingCases 0개
- `npm run judge:lang-audit`: 통과, Python/C++ 제출 가능 경로 유지
- `npm run judge:audit`: 통과, missingCaseSlugs 없음
- `npx next build`: 통과, `/problem/[slug]` 977개 SSG 생성
- `npm run judge:docker-check`: 통과

## 현재 상태

- 총 문제 수: 977개
- 총 override 수: 977개
- 남은 확장 후보 수: 33개
- 다음 배치는 남은 고난도 문제를 20개 이하 단위로 이어서 처리한다.
