import { expect, test, type Page } from "@playwright/test";

async function resetSession(page: Page) {
  await page.context().clearCookies();
  await page.goto("/login");
  await page.evaluate(() => {
    window.localStorage.clear();
    window.sessionStorage.clear();
  });
}

async function startGuest(page: Page) {
  await page.goto("/login");
  await expect(page.getByTestId("guest-start")).toBeVisible();
  await page.getByTestId("guest-start").click();
  await expect(page).toHaveURL(/\/$/);
}

test.beforeEach(async ({ page }) => {
  await resetSession(page);
});

test("Guest 사용자는 로그인 페이지에서 바로 체험을 시작하고 Guest 상태를 확인할 수 있다", async ({ page }) => {
  await expect(page.getByTestId("guest-start")).toHaveText(/게스트로 체험하기/);

  await startGuest(page);
  await page.goto("/profile");

  await expect(page.getByTestId("guest-status")).toContainText("Guest");
  await expect(page.getByTestId("guest-status")).toContainText("체험 중");
  await expect(page.getByTestId("save-records-cta")).toHaveText("로그인하고 저장하기");
});

test("Guest 상태에서도 기본 문제 풀이 기능에 접근할 수 있고 계정 저장 기능은 로그인 CTA로 제한된다", async ({ page }) => {
  await startGuest(page);

  await page.goto("/problem/string-1152");
  await expect(page.getByTestId("code-editor")).toBeVisible();
  await expect(page.getByTestId("submit-solution")).toBeEnabled();

  await page.goto("/profile");
  await page.getByTestId("save-records-cta").click();
  await expect(page.getByTestId("auth-required-modal")).toBeVisible();
  await expect(page.getByTestId("kakao-login")).toHaveText("카카오로 로그인");
});

test("Guest 사용자는 카카오 mock OAuth 이후 기존 트레이너 기록을 로그인 계정에 연결한다", async ({ page }) => {
  await startGuest(page);

  await page.goto("/profile");
  const guestName = await page.locator("text=/Guest\\d+/").first().textContent();
  await page.getByTestId("save-records-cta").click();
  await page.getByTestId("kakao-login").click();

  await expect(page).toHaveURL(/\/profile\?auth=linked/);
  await expect(page.getByTestId("auth-status")).toContainText("로그인됨");
  await expect(page.getByTestId("linked-accounts")).toContainText("카카오 연결됨");
  await expect(page.getByTestId("linked-accounts")).toContainText("E2E 카카오 사용자");
  if (guestName) {
    await expect(page.getByText(guestName.trim()).first()).toBeVisible();
  }

  const accounts = await page.request.get("/api/auth/accounts");
  expect(accounts.ok()).toBeTruthy();
  const body = await accounts.json();
  expect(body.accounts?.[0]?.provider).toBe("kakao");
});

test("로그인 완료 후 Guest CTA는 사라지고 보호된 프로필 영역에 접근할 수 있다", async ({ page }) => {
  await startGuest(page);

  await page.goto("/profile");
  await page.getByTestId("save-records-cta").click();
  await page.getByTestId("kakao-login").click();

  await expect(page.getByTestId("auth-status")).toBeVisible();
  await expect(page.getByTestId("guest-status")).toHaveCount(0);
  await expect(page.getByTestId("save-records-cta")).toHaveCount(0);
  await expect(page.getByTestId("protected-profile-link")).toBeVisible();
});
