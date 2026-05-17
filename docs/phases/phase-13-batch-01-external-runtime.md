# Phase 13 Batch 01. 외부 풀이 런타임 후보

## 목표

외부 풀이 링크가 있고, 그중 Python 또는 C++ 코드가 확인된 문제를 1차 편입 후보로 묶는다.

이 batch는 아직 서비스 편입 완료가 아니다. 정답 코드 파일이 확인되었을 뿐이고, 문제 요약/예제/edge/fuzz 검증을 거쳐야 한다.

## 후보 요약

- 후보 수: 12
- 기준: `data/external-solution-audit.json`에서 `runtime_ready`인 문제
- 상태: 편입 준비 후보

## 후보 목록

| BOJ | slug | 대표 분류 | 언어 |
|---|---|---|---|
| 1238 | shortest_path-1238 | shortest_path | python |
| 1497 | backtracking-1497 | backtracking | cpp |
| 2602 | dynamic_programming_2-2602 | dynamic_programming_2 | cpp |
| 2638 | graph_traversal-2638 | graph_traversal | python |
| 3025 | simulation-3025 | simulation | cpp |
| 11663 | binary_search-11663 | binary_search | cpp |
| 11728 | two_pointer-11728 | two_pointer | java, python |
| 14284 | shortest_path-14284 | shortest_path | cpp, java |
| 14697 | brute_force-14697 | brute_force | cpp |
| 15886 | implementation-15886 | implementation | python |
| 17142 | graph_traversal-17142 | graph_traversal | python |
| 21944 | data_structure2-21944 | data_structure2 | python |

## 편입 전 필수 작업

1. BOJ 원문 링크와 앱용 문제 요약을 작성한다.
2. sample input/output을 확보한다.
3. 외부 정답 코드를 Python/C++ Docker runner에서 실행 검증한다.
4. 문제별 edge/fuzz case를 작성한다.
5. 시간복잡도 함정이 있는 문제는 stress case를 추가한다.
6. 검증 통과 후 `data/problems.json`에 편입하고 `npm run data:map`을 실행한다.

## 실행 결과

- 생성 시각: 2026-05-13T15:47:59.448Z
- 출력: `data/problem-expansion-batch-01.json`

## 다음 단계

이 batch에서 쉬운 문제부터 5개를 골라 실제 문제 요약과 override를 작성한다. 첫 5개는 입출력 안정성과 구현 난이도를 기준으로 고른다.
