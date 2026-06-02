# Phase 25 - Override Expected Output Batch 09

## 목표

브루트포스 override 20개에 문제별 정답 생성기를 추가해서, 샘플/엣지/스트레스 입력이 Python/C++ 제출 모두에서 동일한 expected output으로 채점되도록 고정한다.

이번 배치는 기존 입력 케이스를 유지하고, 각 override 파일 내부에 작은 `_solve()` 함수를 추가하는 방식으로 진행했다. 이렇게 하면 테스트 입력은 그대로 두면서도 oracle 실행 의존도를 줄이고, 제출 언어와 무관하게 같은 정답 문자열을 비교할 수 있다.

## 처리한 문제

- `brute_force-1543`
- `brute_force-1548`
- `brute_force-15661`
- `brute_force-15686`
- `brute_force-15728`
- `brute_force-15779`
- `brute_force-1581`
- `brute_force-15970`
- `brute_force-16508`
- `brute_force-16637`
- `brute_force-1668`
- `brute_force-16937`
- `brute_force-16943`
- `brute_force-16951`
- `brute_force-16986`
- `brute_force-17085`
- `brute_force-1711`
- `brute_force-17471`
- `brute_force-17484`
- `brute_force-17521`

## 구현 내용

- 문자열 탐색, 삼각형 조건, 팀 능력치 차이, 치킨 거리, 카드 제거, 부분수열 길이, 문자열 조합 DP, 색상별 거리, 책 제목 부분집합, 괄호 수식, 트로피 시야, 스티커 배치, 순열 숫자, 등차수열 보정, 가위바위보 순열, 십자가 배치, 직각삼각형 개수, 게리맨더링 연결성, 달 탐사 DP, 주식 매매 시뮬레이션에 대해 expected 생성기를 추가했다.
- `brute_force-16986`은 현재 저장된 정답 코드의 경기 진행 방식과 동일하게 expected를 생성하도록 맞췄다.
- 모든 변경은 override의 입력/출력 레벨에만 머물렀고, judge core나 runner 동작은 변경하지 않았다.

## 검증 결과

실행한 명령:

```bash
python scripts/verify-judge-overrides.py brute_force-1543 brute_force-1548 brute_force-15661 brute_force-15686 brute_force-15728 brute_force-15779 brute_force-1581 brute_force-15970 brute_force-16508 brute_force-16637 brute_force-1668 brute_force-16937 brute_force-16943 brute_force-16951 brute_force-16986 brute_force-17085 brute_force-1711 brute_force-17471 brute_force-17484 brute_force-17521
npm run harness:test
npm run judge:quality
```

결과:

- 타깃 override 20개 모두 self-judge `AC`
- `npm run harness:test`: 20개 테스트 통과
- `npm run judge:quality`: 평균 품질 점수 `64.72`
- expected 누락 현황: `538`문제 / `2180`케이스

## 다음 단계

다음 배치에서는 `brute_force-17610`부터 이어서 expected output을 추가한다. 현재 상위 low-quality 목록에는 아직 expected가 없는 브루트포스 문제와 disjoint set, dynamic programming, shortest path 계열 문제가 남아 있다.
