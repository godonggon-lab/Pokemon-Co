# Phase 13 Batch 03: 그리디 20문제 확장

## 목표

이번 배치는 문제 확장 후보 중 그리디 유형으로 규칙이 명확하고, 입력/출력 기반 oracle을 안정적으로 만들 수 있는 20문제를 먼저 추가했다.

## 추가 문제

- `greedy-1080` 행렬
- `greedy-1343` 폴리오미노
- `greedy-1439` 뒤집기
- `greedy-1449` 수리공 항승
- `greedy-1455` 뒤집기 II
- `greedy-1715` 카드 정렬하기
- `greedy-1744` 수 묶기
- `greedy-1946` 신입 사원
- `greedy-2138` 전구와 스위치
- `greedy-2847` 게임을 만든 동준이
- `greedy-6068` 시간 관리하기
- `greedy-11047` 동전 0
- `greedy-11509` 풍선 맞추기
- `greedy-12782` 비트 우정지수
- `greedy-13413` 오셀로 재배치
- `greedy-14400` 편의점 2
- `greedy-16162` 가희와 3단 고음
- `greedy-16206` 롤케이크
- `greedy-17615` 볼 모으기
- `greedy-19939` 박 터뜨리기

## 구현 내용

- `scripts/import-expansion-manual-batch-11.mjs`로 20문제의 oracle 소스를 `data/problems-extra.json`에 등록했다.
- 각 문제별 `harness/overrides/*.py`를 추가해 최소 입력, 불가능 케이스, 정렬/묶기 경계값, 반복 패턴, stress 입력을 포함했다.
- 사용자 제출 언어는 Python/C++ 모두 같은 입력과 기대 출력으로 검증된다. oracle 소스 언어는 채점 기준 출력을 만들기 위한 내부 구현이다.

## 검증 결과

실행한 명령:

```bash
node scripts/import-expansion-manual-batch-11.mjs
python scripts/verify-judge-overrides.py greedy-1080 greedy-1343 greedy-1439 greedy-1449 greedy-1455 greedy-1715 greedy-1744 greedy-1946 greedy-2138 greedy-2847 greedy-6068 greedy-11047 greedy-11509 greedy-12782 greedy-13413 greedy-14400 greedy-16162 greedy-16206 greedy-17615 greedy-19939
npm run data:map
npm run judge:coverage
npm run judge:lang-audit
npm run judge:audit
npx next build
```

결과:

- 신규 20문제 override self-judge: 모두 AC
- 전체 포켓몬 매핑: 497개
- judge coverage: 497개 전부 judge ready
- missing case: 0개
- Python/C++ 제출 가능성 audit: 통과
- Next.js build: 통과

## 남은 작업량

- 확장 후보 파일 기준 남은 문제: 507개
- 다음 배치부터도 20개 단위로 처리하고, 각 배치 종료 시 commit/push한다.
