import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  fullyParallel: false,
  workers: 1,
  retries: 0,
  reporter: [["list"]],
  use: {
    baseURL: process.env.E2E_BASE_URL ?? "http://localhost:3000",
    headless: true,
    viewport: { width: 1280, height: 800 }
  },
  webServer: process.env.E2E_NO_SERVER
    ? undefined
    : {
        command: "npm run dev",
        url: "http://localhost:3000",
        reuseExistingServer: true,
        timeout: 120_000,
        env: {
          ...process.env,
          E2E_MOCK_OAUTH: "1",
          KAKAO_REST_API_KEY: process.env.KAKAO_REST_API_KEY || "e2e-kakao-rest-key",
          KAKAO_REDIRECT_URI: process.env.KAKAO_REDIRECT_URI || "http://localhost:3000/api/auth/kakao/callback"
        }
      }
});
