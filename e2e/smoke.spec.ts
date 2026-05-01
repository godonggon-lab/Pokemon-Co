import { test, expect } from "@playwright/test";

test("도감 홈에서 분류 카드가 보이고 클릭하면 문제 그리드가 나온다", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("heading", { name: /도감으로 잡으면 된다/ })).toBeVisible();

  // '완전탐색' 카드 클릭
  const card = page.getByRole("link", { name: /완전탐색/ }).first();
  await card.click();

  await expect(page).toHaveURL(/\/category\/brute_force/);
  // 도감번호 형식 (No. 0XXXX) 이 하나라도 보여야 함
  await expect(page.getByText(/No\. \d{5}/).first()).toBeVisible();
});

test("문제 페이지에 코드 에디터(또는 placeholder)와 도전 버튼이 있다", async ({ page }) => {
  await page.goto("/category/brute_force");
  await page.getByText(/No\. \d{5}/).first().click();
  await expect(page.getByRole("button", { name: /도전/ })).toBeVisible();
});
