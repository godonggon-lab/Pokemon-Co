# Phase 01. 한글 인코딩과 UI 문구 점검

## 목표

README, UI 문구, 주석, 테스트명이 실제 파일 기준으로 UTF-8 한국어인지 확인합니다. PowerShell 콘솔에서는 한글이 깨져 보일 수 있으므로, 파일 자체의 인코딩과 콘솔 표시 문제를 분리해서 판단합니다.

## 범위

- `README.md` UTF-8 확인
- `judge/README.md` UTF-8 확인
- 주요 화면 문구 확인
  - `app/page.tsx`
  - `app/problems/page.tsx`
  - `app/problem/[slug]/page.tsx`
  - `app/category/[slug]/page.tsx`
  - `app/profile/page.tsx`
  - `app/leaderboard/page.tsx`
- 주요 컴포넌트 문구 복구
  - `components/ProblemPlayground.tsx`
  - `components/TrainerHUD.tsx`
  - `components/FlavorBody.tsx`
- Playwright 테스트 문구 복구
- UTF-8 저장 상태 확인
- `.editorconfig` 추가

## 완료 기준

- 주요 문서와 UI 파일을 UTF-8로 읽을 수 있다.
- 유니코드 replacement character(`�`)가 없다.
- 앞으로 편집기가 UTF-8/LF를 기본으로 쓰도록 `.editorconfig`가 있다.
- `npm run build`가 통과한다.

## 작업 로그

- Python으로 주요 파일을 UTF-8로 직접 읽어 실제 문자열을 확인했다.
- PowerShell `Get-Content` 출력이 깨지는 것은 콘솔 인코딩 표시 문제임을 확인했다.
- 전체 주요 소스/문서 파일에서 replacement character(`�`)를 검사했다.
- `.editorconfig`를 추가해 UTF-8, LF, final newline을 기본 규칙으로 지정했다.
- Markdown은 줄 끝 공백이 의미를 가질 수 있어 `trim_trailing_whitespace = false`로 예외 처리했다.
- `npm run build`로 production build를 재확인했다.

## 실행 결과(Output)

### 1. 실제 UTF-8 문구 확인

명령:

```bash
$env:PYTHONIOENCODING='utf-8'
python - <<'PY'
from pathlib import Path
for path in ['README.md','judge/README.md','app/problems/page.tsx']:
    print(Path(path).read_text(encoding='utf-8').splitlines()[:5])
PY
```

결과 요약:

```text
README.md: "# DongJun CodeDex 🎮", "백준이 닫혀서 만든..."
judge/README.md: "# DongJun CodeDex 채점 인프라"
app/problems/page.tsx: "전체 문제", "분류", "언어", "바로가기"
```

판단:

- 파일 자체는 UTF-8 한국어로 정상 저장되어 있다.
- PowerShell 기본 출력에서 보이는 깨짐은 파일 손상이 아니다.

### 2. replacement character 검사

명령:

```bash
python - <<'PY'
from pathlib import Path
bad = []
for p in Path('.').rglob('*'):
    if any(part in {'.git','node_modules','.next','.data'} for part in p.parts):
        continue
    if p.is_file() and p.suffix in {'.ts','.tsx','.md','.py','.mjs','.json','.css','.sh'}:
        text = p.read_text(encoding='utf-8')
        if '\ufffd' in text:
            bad.append(str(p))
print('bad_count', len(bad))
PY
```

결과:

```text
bad_count 0
```

판단:

- UTF-8 디코딩 실패 흔적인 `�` 문자는 발견되지 않았다.
- 따라서 대규모 문구 복구 작업은 현재 필요하지 않다.

### 3. 추가한 파일

```text
.editorconfig
```

내용 요약:

```text
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
```

판단:

- 이후 VS Code 등 편집기에서 파일을 열고 저장할 때 UTF-8/LF 기준을 유지하기 쉬워졌다.

### 4. Production build 확인

명령:

```bash
npm run build
```

결과 요약:

```text
[index-boj] categories: 22, problems: 362
[pokedex] using cached data/pokedex.json (1025 entries)
[monster-map] 362 mappings
✓ Compiled successfully
✓ Generating static pages (392/392)
```

판단:

- `.editorconfig` 추가 후에도 build는 정상 통과한다.
- Phase 01 변경은 런타임 동작을 바꾸지 않는 개발 환경/문서 정리 변경이다.

## 예상 리스크

- PowerShell에서 `Get-Content`로 한글이 깨져 보여도 실제 파일은 정상일 수 있습니다.
- 콘솔에서 확인할 때는 `PYTHONIOENCODING=utf-8` 또는 UTF-8 capable terminal을 사용하는 편이 안전합니다.
