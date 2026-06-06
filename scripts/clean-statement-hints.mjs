import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { cleanHintText } from "./fetch-boj-statements.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const STATEMENTS_PATH = path.join(ROOT, "data", "problems-statements.json");

const statements = JSON.parse(await readFile(STATEMENTS_PATH, "utf8"));
let changed = 0;

for (const statement of Object.values(statements)) {
  if (!statement || typeof statement !== "object" || typeof statement.hint !== "string") {
    continue;
  }
  const cleaned = cleanHintText(statement.hint);
  if (cleaned !== statement.hint) {
    statement.hint = cleaned;
    changed += 1;
  }
}

await writeFile(STATEMENTS_PATH, JSON.stringify(statements), "utf8");
console.log(`[statement-hints] cleaned: ${changed}`);
