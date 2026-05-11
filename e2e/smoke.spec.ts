import { expect, test, type Page } from "@playwright/test";

async function enterAsGuest(page: Page) {
  await page.goto("/login");
  await page.getByTestId("guest-start").click();

  const input = page.getByTestId("trainer-name-input");
  await expect(input).toBeVisible();
  await input.fill(`테스터${Date.now()}`.slice(0, 16));
  await page.getByTestId("trainer-name-submit").click();
  await expect(input).toBeHidden();
}

test("도감 홈에서 분류 카드가 보이고 클릭하면 문제 그리드가 나온다", async ({ page }) => {
  await page.context().clearCookies();
  await enterAsGuest(page);
  await expect(page.getByRole("heading", { name: /잡아서 성장하자/ })).toBeVisible();

  const card = page.getByRole("link", { name: /완전탐색/ }).first();
  await card.click();

  await expect(page).toHaveURL(/\/category\/brute_force/);
  await expect(page.getByText(/No\. \d{4,5}/).first()).toBeVisible();
});

test("문제 페이지에 코드 에디터와 제출 버튼이 있다", async ({ page }) => {
  await page.context().clearCookies();
  await enterAsGuest(page);
  await page.goto("/category/brute_force");
  await page.getByText(/No\. \d{4,5}/).first().click();
  await expect(page.getByRole("button", { name: /도전/ })).toBeVisible();
});
