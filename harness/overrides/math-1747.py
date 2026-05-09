from __future__ import annotations

from math import isqrt
from typing import List

from harness.cases import GeneratedCase, edge, stress


def is_prime(x: int) -> bool:
    return x >= 2 and all(x % d for d in range(2, isqrt(x) + 1))


def expected(stdin: str) -> str:
    x = int(stdin)
    while True:
        if str(x) == str(x)[::-1] and is_prime(x):
            return f"{x}\n"
        x += 1


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "2\n", "31\n", "100\n", "998\n", "1000000\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
