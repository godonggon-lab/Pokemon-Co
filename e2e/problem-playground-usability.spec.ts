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

async function openProblem(page: Page) {
  await enterAsGuest(page);
  await page.goto("/problem/string-1152");
  await expect(page.getByTestId("code-editor")).toBeVisible();
  await expect(page.getByTestId("submit-solution")).toBeEnabled();
}

async function replaceEditorText(page: Page, code: string) {
  const editor = page.getByTestId("code-editor");
  await editor.click();
  await page.keyboard.press("ControlOrMeta+A");
  await page.keyboard.insertText(code);
}

test("문제 풀이 화면에서 언어 선택, 코드 자동 저장, 직접 입력이 막히지 않는다", async ({ page }) => {
  await openProblem(page);

  await expect(page.getByLabel("풀이 언어")).toHaveValue("python");
  await page.getByLabel("풀이 언어").selectOption("cpp");
  await expect(page.getByLabel("풀이 언어")).toHaveValue("cpp");
  await page.getByLabel("풀이 언어").selectOption("python");

  const code = "import sys\nprint(len(sys.stdin.read().split()))\n";
  await replaceEditorText(page, code);
  await expect.poll(async () => {
    return page.evaluate(() => window.localStorage.getItem("codedex:draft:string-1152:python"));
  }).toContain("sys.stdin.read");

  await page.getByLabel("직접 실행 입력").fill("hello world\n");
  await expect.poll(async () => {
    return page.evaluate(() => window.localStorage.getItem("codedex:stdin:string-1152"));
  }).toBe("hello world\n");
});

test("직접 실행 결과는 stdout과 상태를 사용자가 확인할 수 있게 보여준다", async ({ page }) => {
  await page.route("**/api/judge", async (route) => {
    const body = route.request().postDataJSON();
    expect(body.mode).toBe("run");
    await route.fulfill({
      contentType: "application/json",
      body: JSON.stringify({
        status: "OK",
        stdout: "2\n",
        stderr: "",
        durationMs: 12,
        exitCode: 0
      })
    });
  });

  await openProblem(page);
  await replaceEditorText(page, "import sys\nprint(len(sys.stdin.read().split()))\n");
  await page.getByLabel("직접 실행 입력").fill("hello world\n");
  await page.getByTestId("run-custom-input").click();

  await expect(page.getByTestId("run-status")).toHaveText("OK");
  await expect(page.getByTestId("run-panel")).toContainText("2");
  await expect(page.getByTestId("run-panel")).toContainText("stdout");
});

test("제출 결과가 AC와 TLE 모두 명확한 verdict로 표시된다", async ({ page }) => {
  let nextStatus: "AC" | "TLE" = "AC";
  await page.route("**/api/judge", async (route) => {
    const status = nextStatus;
    await route.fulfill({
      contentType: "application/json",
      body: JSON.stringify({
        status,
        passed: status === "AC" ? 1 : 0,
        total: 1,
        durationMs: status === "AC" ? 20 : 1000,
        cases: [
          {
            idx: 0,
            input: "hello world\n",
            expected: "2\n",
            actual: status === "AC" ? "2\n" : "<TLE>",
            ok: status === "AC",
            kind: "sample",
            verdict: status
          }
        ]
      })
    });
  });

  await openProblem(page);
  await replaceEditorText(page, "import sys\nprint(len(sys.stdin.read().split()))\n");
  await page.getByTestId("submit-solution").click();
  await expect(page.getByTestId("judge-status")).toContainText("AC");
  await expect(page.getByTestId("verdict-panel")).toContainText("1 / 1");

  nextStatus = "TLE";
  await replaceEditorText(page, "while True:\n    pass\n");
  await page.getByTestId("submit-solution").click();
  await expect(page.getByTestId("judge-status")).toContainText("TLE");
  await expect(page.getByTestId("verdict-panel")).toContainText("<TLE>");
});
