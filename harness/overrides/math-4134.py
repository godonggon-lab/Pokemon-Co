from __future__ import annotations

from math import isqrt
from typing import List

from harness.cases import GeneratedCase, edge, stress


def is_prime(x: int) -> bool:
    return x >= 2 and all(x % d for d in range(2, isqrt(x) + 1))


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    out = []
    for x in nums[1:]:
        while not is_prime(x):
            x += 1
        out.append(str(x))
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n0\n", "1\n2\n", "3\n6\n20\n100\n", "4\n1\n10\n999\n1000\n", "2\n99991\n100000\n", "5\n0\n1\n2\n3\n4\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
