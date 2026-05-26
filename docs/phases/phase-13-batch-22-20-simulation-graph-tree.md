# Phase 13 Batch 22: 시뮬레이션/그래프/트리 20문제 확장

## 목표

이번 배치는 남은 확장 후보 중 BFS, 트리, 시뮬레이션, MST, 백트래킹 문제 20개를 추가했다.
출력이 여러 가지 가능한 문제는 피하고, 숫자/고정 문자열/고정 형식으로 채점 가능한 문제만 포함했다.

## 추가 문제

- `graph_traversal-2234`
- `tree-2250`
- `topological_sorting-3665`
- `trie-5670`
- `graph_traversal-6087`
- `tree-6416`
- `backtracking-7682`
- `tree-9489`
- `tree-12896`
- `simulation-13459`
- `simulation-13460`
- `minimum_spanning_tree-13905`
- `backtracking-13908`
- `shortest_path-13911`
- `tree-14657`
- `simulation-15653`
- `backtracking-15684`
- `simulation-15685`
- `graph_traversal-16988`
- `simulation-17135`

## 검증 명령

```bash
node scripts/import-expansion-manual-batch-30.mjs
python scripts/verify-judge-overrides.py graph_traversal-2234 tree-2250 topological_sorting-3665 trie-5670 graph_traversal-6087 tree-6416 backtracking-7682 tree-9489 tree-12896 simulation-13459 simulation-13460 minimum_spanning_tree-13905 backtracking-13908 shortest_path-13911 tree-14657 simulation-15653 backtracking-15684 simulation-15685 graph_traversal-16988 simulation-17135
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
npm run judge:docker-check
```

## 검증 결과

- 신규 20문제 override self-judge: 모두 AC
- 전체 문제 수: 877개
- judge coverage: 877개 모두 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js production build: 통과
- Docker runner check: 재실행 통과

## 참고

- Docker smoke test가 첫 실행에서 C++ 빈 출력으로 한 번 흔들렸지만, 동일 명령 재실행은 통과했다. 이번 배치의 override self-judge, coverage, build는 모두 통과했으므로 데이터 변경 자체의 문제는 아니다.
- 시뮬레이션 문제는 작은 edge/stress 케이스를 섞어 이동 순서, 충돌 처리, 실패 케이스를 함께 확인하도록 구성했다.

## 현재 상태

- 이번 배치 처리: 20개
- 전체 문제 수: 877개
- 확장 후보 기준 남은 문제: 127개
