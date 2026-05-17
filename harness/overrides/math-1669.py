from __future__ import annotations

import math
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    x, y = map(int, stdin.split())
    d = y - x
    if d == 0:
        return "0"
    k = math.isqrt(d)
    if k * k == d:
        return str(2 * k - 1)
    if d <= k * k + k:
        return str(2 * k)
    return str(2 * k + 1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "0 0\n",
        "0 1\n",
        "0 2\n",
        "0 3\n",
        "0 4\n",
        "45 50\n",
        "1 1000000000\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
