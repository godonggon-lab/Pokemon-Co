import assert from "node:assert/strict";
import test from "node:test";

import { cleanHintText, extractSection, stripTags } from "../fetch-boj-statements.mjs";

test("stripTags removes non-visible script payloads", () => {
  const encodedJson = "eyJoaW50Ijoi7JWE64uI7JWEIn0=";
  const html = `<p>실제 힌트</p><script type="application/json">${encodedJson}</script>`;

  const result = stripTags(html, "20240101000000");

  assert.equal(result, "실제 힌트");
  assert.doesNotMatch(result, /eyJoaW50/);
});

test("extractSection ignores script data inside problem_hint", () => {
  const html = `
    <section id="problem_hint">
      <p>두 수의 차이를 확인한다.</p>
      <script>window.__DATA__ = "QmFzZTY0SlNPTg==";</script>
    </section>
    <section id="problem_input"><p>입력</p></section>
  `;

  assert.equal(
    extractSection(html, "problem_hint", "20240101000000"),
    "두 수의 차이를 확인한다."
  );
});

test("cleanHintText preserves visible hint before a Base64 payload", () => {
  const payload = "W3sicHJvYmxlbV9pZCI6IjE2OTciLCJwcm9ibGVtX2xhbmciOiIwIiwidGl0bGUiOiJ0ZXN0IiwiaGludCI6ImVtYmVkZGVkLWpzb24tcGF5bG9hZCJ9XQ==";

  assert.equal(
    cleanHintText(`수빈이는 네 칸을 이동한다. ${payload}`),
    "수빈이는 네 칸을 이동한다."
  );
});
