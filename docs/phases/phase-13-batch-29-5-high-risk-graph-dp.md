# Phase 13 Batch 29 - 고위험 Graph/DP Override 5개 추가

## 목표

남은 후보 중 문제 설명과 출력 형식이 복잡한 편인 DP, 이분 탐색, 그래프 탐색 문제 5개를 작은 배치로 처리했다. 이번 배치는 속도보다 정확도를 우선했고, 각 문제별 oracle과 override 입력을 먼저 검증한 뒤 전체 앱 빌드까지 확인했다.

## 추가한 문제

- `dynamic_programming_2-13707`
- `binary_search-20495`
- `graph_traversal-22946`
- `graph_traversal-22948`
- `graph_traversal-22949`

## 작업 내용

- 각 문제에 `harness/overrides/*.py` 파일을 추가했다.
- `scripts/import-expansion-manual-batch-37.mjs`로 5개 문제의 metadata와 Python oracle을 `data/problems-extra.json`에 반영했다.
- `graph_traversal-22946`, `graph_traversal-22948`은 원 포함 관계를 트리로 만든 뒤 지름 또는 경로를 계산하도록 oracle을 작성했다.
- `graph_traversal-22949`는 4x4 구역 회전 상태를 4단계로 전처리하고, 현재 회전 상태와 좌표를 함께 방문 처리하는 BFS oracle을 추가했다.
- `npm run problems:expansion-audit`를 다시 실행해 남은 후보 목록을 갱신했다.

## 검증 결과

- `python scripts/verify-judge-overrides.py dynamic_programming_2-13707 binary_search-20495 graph_traversal-22946 graph_traversal-22948 graph_traversal-22949`: 통과
- `npm run data:map`: 통과, monster mapping 992개
- `npm run judge:coverage`: 통과, judgeReady 992개, missingCases 0개
- `npm run judge:lang-audit`: 통과, Python/C++ 제출 가능 경로 유지
- `npm run judge:audit`: 통과, missingCaseSlugs 없음
- `npm run judge:docker-check`: 통과
- `npx next build`: 통과, `/problem/[slug]` 992개 SSG 생성
- `npm run problems:expansion-audit`: 통과, 남은 후보 18개

## 현재 상태

- 총 judge-ready 문제 수: 992개
- 총 override 수: 992개
- 남은 확장 후보: 18개

남은 문제들은 외부 정답/해설 단서가 적거나 문제 포맷이 오래된 유형이 많다. 다음 배치부터는 20개 단위보다 더 작게 쪼개서, 문제별 입력 형식 확인 후 oracle을 작성하는 편이 안전하다.
