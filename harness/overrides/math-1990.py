from __future__ import annotations

from math import isqrt
from typing import List

from harness.cases import GeneratedCase, edge, stress


def is_prime(x: int) -> bool:
    return x >= 2 and all(x % d for d in range(2, isqrt(x) + 1))


def expected(stdin: str) -> str:
    a, b = map(int, stdin.split())
    out = [str(x) for x in range(a, b + 1) if str(x) == str(x)[::-1] and is_prime(x)]
    out.append("-1")
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1 10\n", "10 100\n", "100 200\n", "2 2\n", "998 10301\n", "1 100000\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
