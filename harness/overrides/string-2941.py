from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


TOKENS = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


def _solve(stdin: str) -> str:
    s = stdin.strip()
    for token in TOKENS:
        s = s.replace(token, "*")
    return str(len(s))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "ljes=njak\n",
        "ddz=z=\n",
        "nljj\n",
        "c=c=\n",
        "dz=ak\n",
        "abc\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "c=dz=d-ljnjs=z=abc" * 20
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
