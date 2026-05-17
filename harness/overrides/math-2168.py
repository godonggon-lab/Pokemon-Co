from __future__ import annotations

import math
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    x, y = map(int, stdin.split())
    return str(x + y - math.gcd(x, y))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1 1\n",
        "1 5\n",
        "8 12\n",
        "12 8\n",
        "100000000 99999999\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("123456789 987654321\n", _solve("123456789 987654321\n")))
    return cases
