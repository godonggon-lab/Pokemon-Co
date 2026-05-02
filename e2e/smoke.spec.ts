import { test, expect } from "@playwright/test";

async function completeOnboarding(page: import("@playwright/test").Page) {
  const input = page.getByPlaceholder("예: 동준");
  if (await input.isVisible().catch(() => false)) {
    await input.fill(`테스터${Date.now()}`.slice(0, 16));
    await page.getByRole("button", { name: /모험 시작/ }).click();
    await expect(input).toBeHidden();
  }
}

test("도감 홈에서 분류 카드가 보이고 클릭하면 문제 그리드가 나온다", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("heading", { name: /도감으로 잡으면 된다/ })).toBeVisible();
  await completeOnboarding(page);

  // '완전탐색' 카드 클릭
  const card = page.getByRole("link", { name: /완전탐색/ }).first();
  await card.click();

  await expect(page).toHaveURL(/\/category\/brute_force/);
  // 도감번호 형식 (No. 0001) 이 하나라도 보여야 함
  await expect(page.getByText(/No\. \d{4,5}/).first()).toBeVisible();
});

test("문제 페이지에 코드 에디터(또는 placeholder)와 도전 버튼이 있다", async ({ page }) => {
  await page.goto("/category/brute_force");
  await completeOnboarding(page);
  await page.getByText(/No\. \d{4,5}/).first().click();
  await expect(page.getByRole("button", { name: /도전/ })).toBeVisible();
});
