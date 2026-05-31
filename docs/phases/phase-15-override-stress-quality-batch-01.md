# Phase 15. Override Stress Quality Batch 01

## 목표

1009개 문제 전체 기준으로 override 품질 감사를 확장하고, 시간복잡도 실수가 자주 나는 문제부터 stress case를 보강한다.

## 작업 내용

- `scripts/audit-override-quality.py`가 `data/problems.json`뿐 아니라 `data/problems-extra.json`까지 포함해 1009문제 전체를 감사하도록 수정했다.
- 다음 13개 문제에 stress case를 추가했다.

| 문제 | 유형 | 보강 의도 |
|---|---|---|
| `graph_traversal-17142` | 그래프/BFS 조합 | 바이러스 조합 + BFS 확산 |
| `shortest_path-14284` | 최단경로 | 긴 체인 + 우회 간선 |
| `shortest_path-1507` | 최단경로/Floyd | 다중 최단거리 제거 |
| `shortest_path-20007` | 최단경로 | 왕복 거리 정렬/분할 |
| `topological_sorting-2637` | 위상/DP | 부품 의존 관계 누적 |
| `prefix_sum-17123` | 누적합 | 행/열 갱신 반복 |
| `prefix_sum-10427` | 누적합/정렬 | 여러 구간 비용 계산 |
| `prefix_sum-10713` | 누적합 | 이동 경로 차분 배열 |
| `data_structure2-21944` | 자료구조 | 추천 명령 반복 |
| `data_structure2-19583` | 자료구조/집합 | 출석 로그 대량 교차 |
| `backtracking-1497` | 백트래킹/비트마스크 | 기타 조합 탐색 |
| `brute_force-1034` | 완전탐색 | 중복 행/스위치 parity |
| `math-22943` | 수학/소수 | 순열 + 소수 조건 |

## 실행 결과

```bash
npm run judge:quality
```

- `total`: 1009
- `averageQualityScore`: 60.65
- `missingStressCount`: 27
- `allHaveOverride`: true

```bash
python scripts/verify-judge-overrides.py graph_traversal-17142 shortest_path-14284 shortest_path-1507 shortest_path-20007 topological_sorting-2637 prefix_sum-17123 prefix_sum-10427 prefix_sum-10713 data_structure2-21944 data_structure2-19583 backtracking-1497 brute_force-1034 math-22943
```

- 13개 수정 override 모두 `AC`

```bash
npm run harness:test
```

- 19개 테스트 통과

## 남은 일

- `missingStressCount` 27개를 다음 배치에서 제거한다.
- stress는 단순히 큰 입력을 넣는 것보다, 잘못된 시간복잡도나 자료구조 선택을 드러내는 패턴으로 추가한다.
- 전체 `judge:verify-overrides`는 1009문제라 오래 걸리므로 배치별 targeted verification을 기본으로 사용한다.
