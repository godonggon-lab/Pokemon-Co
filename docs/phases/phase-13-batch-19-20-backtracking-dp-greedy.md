# Phase 13 Batch 19: 백트래킹/DP/그리디 20문제 확장

## 목표

이번 배치는 남은 확장 후보 중 출력이 하나로 결정되는 문제를 우선 골라 20개를 추가했다.
최단 경로 자체를 출력하는 문제처럼 여러 정답이 가능한 special judge 성격의 문제는 이번 배치에서 제외하고, 숫자/문자열/고정 형식 출력 문제 중심으로 구성했다.

## 추가 문제

- `backtracking-10819`
- `backtracking-10971`
- `disjoint_set-12893`
- `backtracking-14888`
- `dynamic_programming_2-14925`
- `shortest_path-14938`
- `brute_force-15686`
- `disjoint_set-16168`
- `dynamic_programming_2-17070`
- `brute_force-17484`
- `backtracking-18290`
- `backtracking-19699`
- `backtracking-19949`
- `greedy-20117`
- `tree-20364`
- `binary_search-20551`
- `greedy-21313`
- `greedy-21314`
- `two_pointer-21921`
- `two_pointer-22862`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-27.mjs
python scripts/verify-judge-overrides.py backtracking-10819 backtracking-10971 disjoint_set-12893 backtracking-14888 dynamic_programming_2-14925 shortest_path-14938 brute_force-15686 disjoint_set-16168 dynamic_programming_2-17070 brute_force-17484 backtracking-18290 backtracking-19699 backtracking-19949 greedy-20117 tree-20364 binary_search-20551 greedy-21313 greedy-21314 two_pointer-21921 two_pointer-22862
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 문제 수: 817개
- judge coverage: 817개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 조정 사항

- `backtracking-19949` oracle은 단순 완전탐색으로도 답은 맞지만 검증 시간이 길어질 수 있어 memoization을 추가했다.
- `shortest_path-14938`의 fuzz 입력에서 도로 개수와 실제 도로 라인 수가 일치하도록 고쳤다.
- Docker Desktop 환경에서 컨테이너 시작 시간이 2초를 넘는 경우가 있어, smoke test의 Python 제한 시간을 10초로 늘렸다. 실제 문제별 채점 제한과 별개로 Docker runner 자체가 정상 작동하는지 확인하기 위한 조정이다.

## 현재 상태

- 이번 배치 처리: 20개
- 전체 문제 수: 817개
- 확장 후보 기준 남은 문제: 187개
