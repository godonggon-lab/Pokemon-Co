from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    if s != s[::-1]:
        return str(len(s))
    if len(set(s)) == 1:
        return "-1"
    return str(len(s) - 1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "ABCBA\n",
        "ABCD\n",
        "AAAA\n",
        "A\n",
        "ABBA\n",
        "AABAA\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "A" * 500 + "B" + "A" * 500
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
