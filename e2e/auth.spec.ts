import { expect, test, type Page } from "@playwright/test";

async function resetSession(page: Page) {
  await page.context().clearCookies();
  await page.goto("/login");
  await page.evaluate(() => {
    window.localStorage.clear();
    window.sessionStorage.clear();
  });
}

async function startGuest(page: Page, name = `테스터${Date.now()}`.slice(0, 16)) {
  await page.goto("/login");
  await expect(page.getByTestId("guest-start")).toBeVisible();
  await expect(page.getByTestId("login-kakao-start")).toBeVisible();
  await page.getByTestId("guest-start").click();

  const input = page.getByTestId("trainer-name-input");
  await expect(input).toBeVisible();
  await input.fill(name);
  await page.getByTestId("trainer-name-submit").click();
  await expect(input).toBeHidden();
  await expect(page).toHaveURL(/\/$/);
  return name;
}

async function completeKakaoSignup(page: Page, name = `카카오${Date.now()}`.slice(0, 16), mockUser = `signup-${Date.now()}`) {
  await page.goto(`/api/auth/kakao/start?mock_user=${mockUser}`);
  await expect(page).toHaveURL(/\/login\?auth=signup_required/);
  await expect(page.getByTestId("trainer-name-input")).toBeVisible();
  await page.getByTestId("trainer-name-input").fill(name);
  await page.getByTestId("trainer-name-submit").click();
  await expect(page).toHaveURL(/\/profile\?auth=linked/);
  await expect(page.getByText(name).first()).toBeVisible();
  await expect(page.getByTestId("auth-status")).toContainText("로그인됨");
  return { name, mockUser };
}

async function replaceEditorText(page: Page, code: string) {
  const editor = page.getByTestId("code-editor");
  await editor.click();
  await page.keyboard.press("ControlOrMeta+A");
  await page.keyboard.insertText(code);
}

test.beforeEach(async ({ page }) => {
  await resetSession(page);
});

test("첫 화면에는 Guest 체험과 카카오 로그인 선택지가 같이 보인다", async ({ page }) => {
  await page.goto("/");
  await expect(page).toHaveURL(/\/login$/);
  await expect(page.getByTestId("login-kakao-start")).toContainText("카카오");
  await expect(page.getByTestId("guest-start")).toContainText("체험");
});

test("Guest 사용자는 오박사의 이름 확인 후 체험을 시작하고 Guest 상태를 확인할 수 있다", async ({ page }) => {
  const trainerName = await startGuest(page);
  await page.goto("/profile");

  await expect(page.getByText(trainerName).first()).toBeVisible();
  await expect(page.getByTestId("guest-status")).toContainText("체험 중");
  await expect(page.getByTestId("save-records-cta")).toContainText("카카오");
});

test("카카오 신규 계정은 로그인 후 닉네임 입력으로 프로필을 생성한다", async ({ page }) => {
  const { name } = await completeKakaoSignup(page);

  await expect(page.getByText(name).first()).toBeVisible();
  await expect(page.getByTestId("guest-status")).toHaveCount(0);

  const accounts = await page.request.get("/api/auth/accounts");
  expect(accounts.ok()).toBeTruthy();
  const body = await accounts.json();
  expect(body.accounts?.[0]?.provider).toBe("kakao");
});

test("이미 카카오로 로그인된 사용자가 로그인 페이지에 가면 Guest 시작 대신 기존 세션을 이어간다", async ({ page }) => {
  const { name } = await completeKakaoSignup(page);

  await page.goto("/login");
  await expect(page.getByTestId("login-authenticated-session")).toBeVisible();
  await expect(page.getByTestId("login-current-session")).toContainText(name);
  await expect(page.getByTestId("guest-start")).toHaveCount(0);
  await expect(page.getByTestId("login-kakao-start")).toHaveCount(0);
});

test("Guest 세션 사용자가 로그인 페이지에 가면 카카오 로그인은 보이고 Guest 시작은 숨겨진다", async ({ page }) => {
  const name = await startGuest(page);

  await page.goto("/login");
  await expect(page.getByTestId("login-guest-session")).toBeVisible();
  await expect(page.getByTestId("login-current-session")).toContainText(name);
  await expect(page.getByTestId("login-kakao-start")).toContainText("카카오");
  await expect(page.getByTestId("guest-start")).toHaveCount(0);
});

test("Guest 상태에서도 기본 문제 풀이 기능에 접근할 수 있고 계정 저장 기능은 로그인 CTA로 제한된다", async ({ page }) => {
  await startGuest(page);

  await page.goto("/problem/string-1152");
  await expect(page.getByTestId("code-editor")).toBeVisible();
  await expect(page.getByTestId("submit-solution")).toBeEnabled();

  await page.goto("/profile");
  await page.getByTestId("save-records-cta").click();
  await expect(page.getByTestId("auth-required-modal")).toBeVisible();
  await expect(page.getByTestId("kakao-login")).toContainText("카카오");
});

test("Guest 사용자는 카카오 mock OAuth 이후 현재 트레이너 기록을 새 로그인 계정에 연결한다", async ({ page }) => {
  const trainerName = await startGuest(page);

  await page.goto("/profile");
  await page.getByTestId("save-records-cta").click();
  await page.getByTestId("kakao-login").click();

  await expect(page).toHaveURL(/\/profile\?auth=linked/);
  await expect(page.getByTestId("auth-status")).toContainText("로그인됨");
  await expect(page.getByTestId("linked-accounts")).toContainText("카카오 연결됨");
  await expect(page.getByTestId("linked-accounts")).toContainText("E2E 카카오 사용자");
  await expect(page.getByText(trainerName).first()).toBeVisible();
});

test("Guest가 문제를 푼 뒤 카카오로 저장해도 포획 기록이 유지된다", async ({ page }) => {
  await page.route("**/api/judge", async (route) => {
    await route.fulfill({
      contentType: "application/json",
      body: JSON.stringify({
        status: "AC",
        passed: 1,
        total: 1,
        durationMs: 12,
        cases: [
          {
            idx: 0,
            input: "hello world\n",
            expected: "2\n",
            actual: "2\n",
            ok: true,
            kind: "sample",
            verdict: "AC"
          }
        ]
      })
    });
  });

  await startGuest(page);
  await page.goto("/problem/string-1152");
  await replaceEditorText(page, "import sys\nprint(len(sys.stdin.read().split()))\n");
  await page.getByTestId("submit-solution").click();
  await expect(page.getByTestId("judge-status")).toContainText("AC");

  await expect.poll(async () => {
    const before = await (await page.request.get("/api/trainer")).json();
    return before.captures?.some((c: any) => c.problemSlug === "string-1152") ?? false;
  }).toBeTruthy();

  await page.goto("/profile");
  await page.getByTestId("save-records-cta").click();
  await page.getByTestId("kakao-login").click();
  await expect(page).toHaveURL(/\/profile\?auth=linked/);

  const after = await (await page.request.get("/api/trainer")).json();
  expect(after.captures?.some((c: any) => c.problemSlug === "string-1152")).toBeTruthy();
});

test("이미 연결된 카카오 계정으로 로그인하면 새 Guest가 아니라 기존 트레이너 프로필을 복구한다", async ({ page }) => {
  const { name: originalName, mockUser } = await completeKakaoSignup(page, `원본${Date.now()}`.slice(0, 16));

  await page.getByTestId("logout-button").click();
  await expect(page).toHaveURL(/\/login/);
  await expect(page.getByTestId("guest-start")).toBeVisible();

  const temporaryGuestName = await startGuest(page, `임시${Date.now()}`.slice(0, 16));
  await page.goto("/profile");
  await expect(page.getByText(temporaryGuestName).first()).toBeVisible();

  await page.goto(`/api/auth/kakao/start?mock_user=${mockUser}`);
  await expect(page).toHaveURL(/\/profile\?auth=signed_in/);
  await expect(page.getByText(originalName).first()).toBeVisible();
  await expect(page.getByText(temporaryGuestName).first()).toHaveCount(0);
});

test("로그인 완료 후 Guest CTA는 사라지고 로그아웃할 수 있다", async ({ page }) => {
  await completeKakaoSignup(page);

  await expect(page.getByTestId("auth-status")).toBeVisible();
  await expect(page.getByTestId("guest-status")).toHaveCount(0);
  await expect(page.getByTestId("save-records-cta")).toHaveCount(0);
  await expect(page.getByTestId("protected-profile-link")).toBeVisible();

  await page.getByTestId("logout-button").click();
  await expect(page).toHaveURL(/\/login/);
  await expect(page.getByTestId("guest-start")).toBeVisible();
});
