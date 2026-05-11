# 카카오 OAuth 로그인 설정 가이드

## 개요

카카오 소셜 로그인의 redirect URI 설정과 localhost/127.0.0.1 쿠키 문제 해결 과정을 기록한다.

## 핵심 원칙

**브라우저는 `localhost`와 `127.0.0.1`을 별도 도메인으로 취급한다.**

따라서 한쪽에서 설정한 쿠키는 다른 쪽에서 읽을 수 없다.
OAuth 콜백 시 state 쿠키와 세션 쿠키가 동일 도메인에서 읽혀야 하므로,
**하나의 호스트로 통일**하는 것이 필수다.

## 환경별 redirect URI 분리

| 파일 | 용도 | 자동 로드 조건 |
|---|---|---|
| `.env` | 공통 설정 (API 키, 시크릿 등) | 항상 |
| `.env.development` | 개발 전용 redirect URI | `npm run dev` |
| `.env.production` | 프로덕션 전용 redirect URI | `npm run build && npm start` |

Next.js가 `NODE_ENV`에 따라 자동으로 올바른 파일을 로드한다.

### .env.development
```
KAKAO_REDIRECT_URI=http://localhost:3000/api/auth/kakao/callback
NAVER_REDIRECT_URI=http://localhost:3000/api/auth/naver/callback
```

### .env.production
```
KAKAO_REDIRECT_URI=https://YOUR_DOMAIN/api/auth/kakao/callback
NAVER_REDIRECT_URI=https://YOUR_DOMAIN/api/auth/naver/callback
```

## 카카오 개발자 콘솔 설정

[카카오 개발자](https://developers.kakao.com) → 내 애플리케이션 → 카카오 로그인 → Redirect URI

등록해야 할 URI:
- 개발: `http://localhost:3000/api/auth/kakao/callback`
- 프로덕션: `https://YOUR_DOMAIN/api/auth/kakao/callback`

## 과거 문제와 해결

### 문제: `sameOriginLocalRedirect` 함수

`lib/socialAuth.ts`에 있던 `sameOriginLocalRedirect()` 함수가
`.env`에 설정된 redirect URI의 호스트를 요청 origin에 맞게 자동 변환했음.
예: `.env`가 `127.0.0.1` → `localhost`로 접속하면 `localhost`로 변환
→ 카카오 콘솔에 등록된 URI와 불일치 → 인가 에러 발생.

**해결**: 함수를 `.env` 값을 그대로 반환하도록 변경.

### 문제: localhost ↔ 127.0.0.1 쿠키 불일치

1. `localhost:3000`에서 state 쿠키 설정
2. 카카오 콜백이 `127.0.0.1:3000`으로 돌아옴
3. state 쿠키를 못 읽어서 `invalid_state` 에러

**해결**: `.env`와 카카오 콘솔 모두 `localhost`로 통일.
미들웨어로 리다이렉트하는 방식은 과한 해결책이므로 채택하지 않음.

## OAuth 인증 흐름

```
사용자 → /api/auth/kakao/start
  → state 생성 + 쿠키에 저장
  → 카카오 인증 페이지로 리다이렉트

카카오 → /api/auth/kakao/callback?code=...&state=...
  → state 쿠키 검증
  → 토큰 교환 → 프로필 조회
  → 기존 유저면 세션 쿠키 설정 + /profile로 리다이렉트
  → 새 유저면 /login?auth=signup_required로 리다이렉트 (이름 입력)
```

## 체크리스트

- [ ] `.env.development`에 redirect URI가 `localhost`로 설정됨
- [ ] 카카오 콘솔에 `http://localhost:3000/api/auth/kakao/callback` 등록됨
- [ ] 프로덕션 배포 시 `.env.production`에 실제 도메인 설정
- [ ] 카카오 콘솔에 프로덕션 도메인 redirect URI 추가 등록
