from __future__ import annotations

from math import gcd
from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    a, b = map(int, stdin.split())
    g = gcd(a, b)
    return f"{g}\n{a * b // g}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1 1\n", "2 3\n", "6 8\n", "12 18\n", "100 25\n", "999 37\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
