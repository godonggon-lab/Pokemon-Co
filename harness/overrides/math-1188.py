from __future__ import annotations

import math
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n, m = map(int, stdin.split())
    return str(m - math.gcd(n, m))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1 1\n",
        "2 2\n",
        "2 3\n",
        "4 6\n",
        "10 4\n",
        "999999999 1000000000\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("123456789 987654321\n", _solve("123456789 987654321\n")))
    return cases
