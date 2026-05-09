import type { AuthProvider } from "./db";

export type SocialProfile = {
  provider: AuthProvider;
  providerUserId: string;
  email?: string | null;
  displayName?: string | null;
};

type ProviderConfig = {
  clientId: string;
  clientSecret?: string;
  redirectUri: string;
  authorizeUrl: string;
  tokenUrl: string;
  profileUrl: string;
};

export function parseProvider(value: string): AuthProvider | null {
  return value === "kakao" || value === "naver" ? value : null;
}

export function providerLabel(provider: AuthProvider) {
  return provider === "kakao" ? "카카오" : "네이버";
}

export function providerConfig(provider: AuthProvider): ProviderConfig | null {
  if (provider === "kakao") {
    const clientId = process.env.KAKAO_REST_API_KEY;
    const redirectUri = process.env.KAKAO_REDIRECT_URI;
    if (!clientId || !redirectUri) return null;
    return {
      clientId,
      clientSecret: process.env.KAKAO_CLIENT_SECRET,
      redirectUri,
      authorizeUrl: "https://kauth.kakao.com/oauth/authorize",
      tokenUrl: "https://kauth.kakao.com/oauth/token",
      profileUrl: "https://kapi.kakao.com/v2/user/me"
    };
  }

  const clientId = process.env.NAVER_CLIENT_ID;
  const clientSecret = process.env.NAVER_CLIENT_SECRET;
  const redirectUri = process.env.NAVER_REDIRECT_URI;
  if (!clientId || !clientSecret || !redirectUri) return null;
  return {
    clientId,
    clientSecret,
    redirectUri,
    authorizeUrl: "https://nid.naver.com/oauth2.0/authorize",
    tokenUrl: "https://nid.naver.com/oauth2.0/token",
    profileUrl: "https://openapi.naver.com/v1/nid/me"
  };
}

export function authStateCookie(provider: AuthProvider) {
  return `dj_oauth_state_${provider}`;
}

export function buildAuthorizeUrl(provider: AuthProvider, state: string) {
  const cfg = providerConfig(provider);
  if (!cfg) return null;
  const url = new URL(cfg.authorizeUrl);
  url.searchParams.set("response_type", "code");
  url.searchParams.set("client_id", cfg.clientId);
  url.searchParams.set("redirect_uri", cfg.redirectUri);
  url.searchParams.set("state", state);
  return url;
}

export async function exchangeCodeForProfile(
  provider: AuthProvider,
  code: string
): Promise<SocialProfile> {
  const cfg = providerConfig(provider);
  if (!cfg) throw new Error(`${providerLabel(provider)} 로그인 환경변수가 설정되지 않았습니다.`);

  const form = new URLSearchParams();
  form.set("grant_type", "authorization_code");
  form.set("client_id", cfg.clientId);
  form.set("redirect_uri", cfg.redirectUri);
  form.set("code", code);
  if (cfg.clientSecret) form.set("client_secret", cfg.clientSecret);

  const tokenRes = await fetch(cfg.tokenUrl, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded;charset=utf-8" },
    body: form
  });
  const tokenJson: any = await tokenRes.json().catch(() => ({}));
  if (!tokenRes.ok || !tokenJson.access_token) {
    throw new Error(`${providerLabel(provider)} 토큰 발급 실패`);
  }

  const profileRes = await fetch(cfg.profileUrl, {
    headers: { authorization: `Bearer ${tokenJson.access_token}` }
  });
  const profileJson: any = await profileRes.json().catch(() => ({}));
  if (!profileRes.ok) {
    throw new Error(`${providerLabel(provider)} 프로필 조회 실패`);
  }

  if (provider === "kakao") {
    return {
      provider,
      providerUserId: String(profileJson.id),
      email: profileJson.kakao_account?.email ?? null,
      displayName: profileJson.properties?.nickname ?? profileJson.kakao_account?.profile?.nickname ?? null
    };
  }

  return {
    provider,
    providerUserId: String(profileJson.response?.id ?? ""),
    email: profileJson.response?.email ?? null,
    displayName: profileJson.response?.nickname ?? profileJson.response?.name ?? null
  };
}
