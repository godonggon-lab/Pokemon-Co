# Phase 27 - Override Expected Output Batch 11

## 목표

브루트포스 마지막 묶음과 자료구조 초반 문제의 override에 expected output을 추가한다. 이번 배치부터는 `data_structure` 계열로 넘어가므로, 출력 형식이 중요한 스택/큐/괄호 문제를 우선 안정화한다.

## 처리한 문제

- `brute_force-3085`
- `brute_force-4096`
- `brute_force-5568`
- `brute_force-5671`
- `brute_force-5883`
- `brute_force-7568`
- `brute_force-9094`
- `brute_force-9996`
- `data_structure-1021`
- `data_structure-10828`
- `data_structure-10866`
- `data_structure-1158`
- `data_structure-18258`
- `data_structure-1863`
- `data_structure-1935`
- `data_structure-22866`
- `data_structure-2504`
- `data_structure-2800`
- `data_structure-3986`
- `data_structure-9012`

## 구현 내용

- 사탕 게임, 다음 팰린드롬 수, 카드 조합, 중복 숫자 없는 방 번호, 연속 소 구간, 덩치 순위, 수학 브루트포스, 패턴 매칭 문제에 expected 생성기를 추가했다.
- 회전 큐, 스택, 덱, 요세푸스, 큐, 스카이라인, 후위표기식, 보이는 건물, 괄호값, 괄호 제거, 좋은 단어, VPS 문제에 expected 생성기를 추가했다.
- `brute_force-4096`은 `0990`처럼 앞자리 0이 있는 입력을 고려해서 입력 길이를 유지한 채 다음 팰린드롬까지 증가 횟수를 계산한다.
- `data_structure-22866`은 보이는 건물이 없을 때 출력 줄 끝 공백을 expected에는 넣지 않았다. 채점 비교가 줄 끝 공백을 정규화하므로 실제 정답 코드와 같은 의미로 비교된다.
- expected가 채워진 문제를 테스트 fixture로 쓰면 oracle failure 경로가 사라지므로, oracle 실패 테스트는 아직 expected가 없는 `data_structure2-10546`으로 옮겼다.
- Docker 메모리 제한 테스트는 Windows Docker에서 `oom_killed` 대신 `exit_code=137`로 잡히는 경우를 허용하도록 보정했다.

## 검증 결과

실행한 명령:

```bash
python scripts/verify-judge-overrides.py brute_force-3085 brute_force-4096 brute_force-5568 brute_force-5671 brute_force-5883 brute_force-7568 brute_force-9094 brute_force-9996 data_structure-1021 data_structure-10828 data_structure-10866 data_structure-1158 data_structure-18258 data_structure-1863 data_structure-1935 data_structure-22866 data_structure-2504 data_structure-2800 data_structure-3986 data_structure-9012
npm run harness:test
npm run judge:quality
```

결과:

- 타깃 override 20개 모두 self-judge `AC`
- `npm run harness:test`: 20개 테스트 통과
- `npm run judge:quality`: 평균 품질 점수 `65.52`
- expected 누락 현황: `498`문제 / `1988`케이스

## 다음 단계

다음 배치는 `data_structure2-10546`부터 이어서 처리한다. 이후 `data_structure2`, `disjoint_set`, `divide_and_conquer` 순서로 expected output을 채워간다.
