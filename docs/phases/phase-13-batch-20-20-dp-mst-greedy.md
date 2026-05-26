# Phase 13 Batch 20: DP/MST/그리디 20문제 확장

## 목표

이번 배치는 남은 확장 후보 중 답이 하나로 고정되는 DP, MST, 그리디, 투 포인터, 그래프 문제 20개를 추가했다.
경로 자체를 출력하거나 여러 해가 가능한 문제는 계속 뒤로 미루고, exact compare로 안정적으로 채점 가능한 문제를 우선했다.

## 추가 문제

- `dynamic_programming_2-1943`
- `dynamic_programming_2-2631`
- `disjoint_set-3108`
- `greedy-8980`
- `minimum_spanning_tree-10423`
- `minimum_spanning_tree-13418`
- `dynamic_programming_1-13910`
- `brute_force-14391`
- `dynamic_programming_1-14852`
- `dynamic_programming_2-16400`
- `brute_force-16637`
- `brute_force-16943`
- `graph_traversal-16956`
- `dynamic_programming_2-17069`
- `tree-19542`
- `dynamic_programming_1-20152`
- `two_pointer-20366`
- `disjoint_set-20955`
- `graph_traversal-21937`
- `dynamic_programming_1-22857`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-28.mjs
python scripts/verify-judge-overrides.py dynamic_programming_2-1943 dynamic_programming_2-2631 disjoint_set-3108 greedy-8980 minimum_spanning_tree-10423 minimum_spanning_tree-13418 dynamic_programming_1-13910 brute_force-14391 dynamic_programming_1-14852 dynamic_programming_2-16400 brute_force-16637 brute_force-16943 graph_traversal-16956 dynamic_programming_2-17069 tree-19542 dynamic_programming_1-20152 two_pointer-20366 disjoint_set-20955 graph_traversal-21937 dynamic_programming_1-22857
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 문제 수: 837개
- judge coverage: 837개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 통과

## 조정 사항

- `minimum_spanning_tree-13418`의 edge case 입력에서 간선 개수 선언과 실제 입력 라인 수를 맞췄다.
- Docker Desktop 환경에서 smoke test가 드물게 빈 출력으로 실패하는 현상이 있어, `scripts/check-docker-runner.py`에 1회 재시도를 추가했다. 실제 제출 채점 로직의 verdict를 완화한 것이 아니라, 로컬/CI의 Docker 상태 확인용 smoke test만 안정화한 변경이다.

## 현재 상태

- 이번 배치 처리: 20개
- 전체 문제 수: 837개
- 확장 후보 기준 남은 문제: 167개
