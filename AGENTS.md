# Codex Operating Guidelines

This project uses the following coding-agent rules, adapted from
`forrestchang/andrej-karpathy-skills` (`CLAUDE.md` and `karpathy-guidelines`).

## 1. Think Before Coding

- For non-trivial changes, state the goal, assumptions, and relevant tradeoffs before editing.
- If requirements are ambiguous and a wrong assumption could create rework, ask one concise question.
- For small mechanical changes, proceed directly and keep the process lightweight.

## 2. Simplicity First

- Prefer the smallest implementation that satisfies the current goal.
- Do not add speculative abstractions, new frameworks, or broad refactors unless the current task requires them.
- Match the existing project structure, naming, and style before introducing a new pattern.

## 3. Surgical Changes

- Touch only the files and lines needed for the requested behavior.
- Preserve unrelated user edits and existing worktree changes.
- Do not combine feature work with cleanup unless the cleanup is required to make the feature correct.

## 4. Goal-Driven Execution

- Define what "done" means for the task before or while implementing.
- Verify with the narrowest meaningful checks first, then broader checks when risk requires it.
- For judge and override work, prefer concrete evidence: audit output, targeted verification, and failing-case reproduction.

## 5. DongJun Project Defaults

- Judge correctness is a core product requirement. For judge changes, prioritize deterministic input handling, stable expected output, and clear failure modes.
- Override files should stay problem-specific, reproducible, and language-neutral at the input/output level.
- Documentation should be written in Korean when it explains project planning, phase output, or operational workflow for the owner.
- Deployment docs should distinguish local development, Docker-based judge execution, and future Linux VM/Nginx production deployment.

## Useful Verification Commands

- `npm run judge:coverage`
- `npm run judge:verify-overrides`
- `npm run harness:test`
- `npm run check:env`

Use the command that matches the changed surface area; do not run expensive checks blindly when a targeted check proves the change.
