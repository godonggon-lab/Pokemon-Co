from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def _solve(stdin: str) -> str:
    s = stdin.strip()
    used = [False] * len(s)
    out: list[str] = []

    def build(left: int, right: int) -> None:
        if left > right:
            return
        idx = min(range(left, right + 1), key=lambda i: s[i])
        used[idx] = True
        out.append("".join(s[i] for i in range(len(s)) if used[i]))
        build(idx + 1, right)
        build(left, idx - 1)

    build(0, len(s) - 1)
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["ZOAC\n", "BAC\n", "ABCDE\n", "ALGORITHM\n"]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
