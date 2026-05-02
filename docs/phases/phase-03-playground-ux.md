# Phase 03. 문제 풀이 UX 개선

## 목표

문제 풀이 화면을 실제 연습 도구처럼 편하게 만듭니다. 코드를 잃어버리지 않고, 제출 전 실행해보고, 이전 제출을 다시 확인할 수 있게 합니다.

## 범위

- 문제/언어별 코드 자동 저장
- 언어별 starter template 개선
- `Ctrl+Enter` 제출
- 제출 전 custom input 실행 기능
- 제출 결과 패널 정리
- E2E smoke test 보강

## 완료 기준

- 페이지를 새로고침해도 작성 중인 코드가 유지된다.
- 사용자가 직접 입력한 custom input으로 실행할 수 있다.
- 제출 결과에서 실패 케이스, 예상 출력, 실제 출력이 명확히 보인다.
- 모바일/데스크톱에서 레이아웃이 깨지지 않는다.
- `npm run build`, `npm run harness:test`, `npm run e2e`가 통과한다.

## 작업 로그

- `ProblemPlayground`에 문제/언어별 자동 저장을 추가했다.
  - 저장 키: `codedex:draft:<problemSlug>:<lang>`
  - 직접 실행 입력 저장 키: `codedex:stdin:<problemSlug>`
- Monaco Editor에 `Ctrl/Cmd + Enter` 제출 단축키를 추가했다.
- 직접 실행 입력 textarea와 실행 버튼을 추가했다.
- 직접 실행 결과 패널을 추가했다.
  - `stdout`, `stderr`, 실행 시간, 상태를 분리해서 보여준다.
- `/api/judge`에 `mode: "run"` 요청을 추가했다.
- judge 서버에 `POST /run` endpoint를 추가했다.
- `python judge/server.py` 직접 실행 시 `harness` import가 실패하던 문제를 고쳤다.
- Playwright smoke test를 현재 UI 계약에 맞게 보강했다.
  - 도감 번호는 `No. 0001`처럼 4자리 이상을 허용한다.
  - 온보딩 모달이 있으면 테스트가 트레이너를 먼저 등록한다.
  - 병렬 dev smoke에서 불안정한 Next dev 오류가 있어 직렬 실행으로 바꿨다.

## 실행 결과(Output)

### 1. Production build

명령:

```bash
npm run build
```

결과 요약:

```text
✓ Compiled successfully
✓ Generating static pages (392/392)
```

판단:

- Phase 03 변경 후에도 TypeScript/Next.js production build가 통과한다.
- `/problem/[slug]` 번들 크기는 약 `316 kB`에서 `317 kB`로 소폭 증가했다.

### 2. Harness 테스트

명령:

```bash
npm run harness:test
```

결과:

```text
Ran 5 tests in 2.074s
OK
```

판단:

- Phase 02에서 만든 sample/fuzz 및 ERR 처리 테스트가 유지된다.

### 3. Judge `/run` HTTP smoke

명령 요약:

```bash
JUDGE_USE_DOCKER=0 JUDGE_PORT=5065 python judge/server.py
POST http://127.0.0.1:5065/run
```

요청 요약:

```json
{
  "lang": "python",
  "code": "print(input()[::-1])",
  "stdin": "abc\n"
}
```

결과:

```json
{
  "status": "OK",
  "stdout": "cba\r\n",
  "stderr": "",
  "durationMs": 63,
  "exitCode": 0
}
```

판단:

- custom input 실행용 `/run` endpoint가 실제 HTTP 요청에서 동작한다.
- 테스트 중 `python judge/server.py`가 `harness`를 import하지 못하는 문제가 발견되어 수정했다.

### 4. E2E smoke

첫 실행 결과:

```text
2 failed
```

원인:

- 기존 테스트가 도감번호를 `No. 00000`처럼 5자리로 기대했지만 실제 UI는 `No. 0001`처럼 4자리다.
- 온보딩 모달이 카드 클릭을 막을 수 있었다.
- 병렬 dev smoke에서 Next dev 서버가 `/category/brute_force` 요청 중 내부 오류를 내는 불안정성이 있었다.

조치:

- 도감번호 정규식을 `No. \d{4,5}`로 수정했다.
- 테스트에서 온보딩 모달이 보이면 트레이너를 먼저 등록하도록 했다.
- Playwright `fullyParallel`을 `false`로 바꿨다.

최종 명령:

```bash
npm run e2e
```

최종 결과:

```text
2 passed
```

판단:

- 홈 → 카테고리 → 문제 그리드 흐름이 통과한다.
- 카테고리 → 문제 페이지 → 도전 버튼 확인 흐름이 통과한다.

## 예상 리스크

### 해소/정책 결정 완료

- Monaco Editor 단축키와 브라우저 기본 단축키가 충돌할 수 있습니다.
  - 조치: Monaco의 `editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, ...)`를 사용했다.
  - 판단: 브라우저 기본 제출 단축키에 기대지 않고 Monaco 내부 명령으로 처리한다.
- 제출 기록을 서버 DB에 저장할지 localStorage에 저장할지 결정이 필요했습니다.
  - 정책: 이번 Phase 03에서는 “작성 중 코드 draft”와 “직접 실행 입력”만 localStorage에 저장한다.
  - 제출 이력 DB 저장은 별도 기능으로 분리한다. 이유는 채점 결과/코드 저장 정책이 개인정보와 운영 저장소 정책에 닿기 때문이다.

Phase 03 기준으로 남은 차단 리스크는 없습니다.
