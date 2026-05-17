from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s, p = stdin.strip().splitlines()[:2]
    return "1" if p in s else "0"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "baekjoon\njoo\n",
        "baekjoon\nmoon\n",
        "aaaaa\naaa\n",
        "abcde\nabcde\n",
        "abcde\nf\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "abc" * 1000 + "needle" + "xyz" * 1000
    cases.append(stress(s + "\nneedle\n", _solve(s + "\nneedle\n")))
    return cases
