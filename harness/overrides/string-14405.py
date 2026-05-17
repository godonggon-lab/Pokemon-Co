from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    i = 0
    while i < len(s):
        if s.startswith("pi", i):
            i += 2
        elif s.startswith("ka", i):
            i += 2
        elif s.startswith("chu", i):
            i += 3
        else:
            return "NO"
    return "YES"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "pikapi\n",
        "pipikachu\n",
        "pikaq\n",
        "chupikachupipika\n",
        "p\n",
        "kachupi\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "pikachuchu" * 50
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
