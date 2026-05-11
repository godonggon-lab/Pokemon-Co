# 포켓몬 난이도 매핑 개편 계획

## 목표

현재 문제별 포켓몬 배정은 희귀도 기준이 섞여 있어 난이도 체감이 애매하다. 앞으로는 solved.ac 기준 난이도를 4개 구간으로 접고, 각 구간을 포켓몬 진화 단계와 연결한다.

| solved.ac level | 서비스 등급 | 포켓몬 구성 |
|---:|---|---|
| 1-5 | Bronze | 진화 전 또는 단일 기본 형태 |
| 6-10 | Silver | 1단계 진화 |
| 11-15 | Gold | 2단계 진화 |
| 16 이상 | Platinum | 전설 또는 환상 포켓몬 |

solved.ac에는 Diamond/Ruby 등 더 높은 구간도 있지만, 앱에서는 사용자가 이해하기 쉽도록 Platinum으로 합친다.

## 참고한 자료

- 포켓몬 위키의 전국도감 문서는 전국도감이 모든 포켓몬 정보를 담는 도감이라고 설명하고, 번호순 포켓몬 목록을 제공한다. 예를 들어 1세대 목록은 #0001 이상해씨부터 이어진다.  
  참고: https://pokemon.fandom.com/ko/wiki/%EC%A0%84%EA%B5%AD%EB%8F%84%EA%B0%90
- `godonggon-lab/baekjoon`의 `algorithms` 디렉터리는 알고리즘별 정답 소스/해설 원천으로 사용한다. 현재 앱의 `data/problems.json`도 이 구조와 같은 알고리즘 카테고리 기반이다.  
  참고: https://github.com/godonggon-lab/baekjoon/tree/main/algorithms
- 진화 단계와 전설/환상 여부는 전국도감 표만으로 안정적으로 판별하기 어렵다. 따라서 PokeAPI species/evolution-chain 데이터를 사용해 내부 캐시를 생성한다.

## 적용 방식

### 1. 포켓몬 taxonomy 캐시

새 스크립트:

```bash
npm run data:taxonomy
```

생성 파일:

```text
data/pokemon-taxonomy.json
```

각 포켓몬에 다음 필드를 추가한다.

- `evolutionStage`: 0, 1, 2
- `evolutionClass`: `bronze`, `silver`, `gold`, `platinum`
- `familyRoot`: 진화 계열의 루트 species

일반 빌드에서는 캐시를 재사용하고, 포켓몬 데이터가 바뀌었을 때만 아래 명령으로 갱신한다.

```bash
node scripts/build-pokemon-taxonomy.mjs --refresh
```

### 2. 문제별 포켓몬 배정

새 `build-monster-map` 규칙:

1. 문제의 solved.ac `level`을 읽는다.
2. `level`을 Bronze/Silver/Gold/Platinum으로 변환한다.
3. 같은 등급 안에서 문제는 BOJ 번호 오름차순으로 정렬한다.
4. 같은 등급 포켓몬도 전국도감 번호 오름차순으로 정렬한다.
5. 문제 순서대로 포켓몬을 배정한다.

이렇게 하면 같은 난이도 구간에서는 포켓몬 번호 흐름이 자연스럽게 이어진다.

### 3. 포켓몬 수 부족 처리

현재 데이터 기준:

```text
bronze: 453
silver: 359
gold: 119
platinum: 94
```

현재 문제 분포:

```text
bronze: 45
silver: 164
gold: 149
platinum: 4
```

Gold 문제는 149개인데 2단계 진화 포켓몬은 119마리라서 중복 없는 1:1 배정은 불가능하다. 이 경우 다른 등급 포켓몬으로 내리지 않고 Gold 풀을 전국도감 번호순으로 한 바퀴 더 순환한다. 결과 데이터에는 `reusedPokemon: true`가 남으므로 나중에 Gold 문제 수가 늘거나 포켓몬 정책을 바꾸고 싶을 때 추적할 수 있다.

## 실행 결과

이번 작업에서 실행한 명령:

```bash
node scripts/build-pokemon-taxonomy.mjs --refresh
npm run data:map
npm run e2e
npm run build
```

생성/변경된 핵심 산출물:

- `scripts/build-pokemon-taxonomy.mjs`
- `data/pokemon-taxonomy.json`
- `scripts/build-monster-map.mjs`
- `data/monster-map.json`
- `lib/characters.ts`
- `components/CategoryGrid.tsx`

## 다음 단계

1. `data/pokedex.json`의 한글 이름 인코딩을 점검한다.
2. 문제별 solved.ac 메타데이터가 없는 경우를 줄인다.
3. Gold 구간의 포켓몬 중복을 줄이고 싶다면 다음 정책 중 하나를 선택한다.
   - 2단계 진화만 유지하고 중복 허용
   - 2단계 진화 + 강한 단일 진화 포켓몬을 Gold에 포함
   - Gold 문제 수를 더 엄격한 난이도 기준으로 줄임
4. 문제 해설/정답 원천은 `godonggon-lab/baekjoon/algorithms`를 유지하되, 문제 본문은 브라우저 기반 수집 또는 직접 작성 요약으로 관리한다.
