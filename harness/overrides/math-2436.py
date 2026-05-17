from __future__ import annotations

import math
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    g, l = map(int, stdin.split())
    target = l // g
    best = (g, l)
    for a in range(1, math.isqrt(target) + 1):
        if target % a == 0:
            b = target // a
            if math.gcd(a, b) == 1:
                best = (g * a, g * b)
    return f"{best[0]} {best[1]}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1 1\n",
        "1 10\n",
        "6 180\n",
        "3 60\n",
        "100 100\n",
        "12 720\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("999 999000\n", _solve("999 999000\n")))
    return cases
