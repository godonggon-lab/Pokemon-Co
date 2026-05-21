from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _valid(value: str) -> bool:
    balance = 0
    for ch in value:
        balance += 1 if ch == "(" else -1
        if balance < 0:
            return False
    return balance == 0


def _solve(stdin: str) -> str:
    s = stdin.strip()
    answer = 0
    for i, ch in enumerate(s):
        flipped = s[:i] + (")" if ch == "(" else "(") + s[i + 1 :]
        if _valid(flipped):
            answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["()(())))\n", "())(\n", "((())\n", "()()\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "(" * 51 + ")" * 49 + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
