from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    n, r, c = map(int, stdin.split())
    ans = 0
    while n:
        half = 1 << (n - 1)
        ans += (r // half * 2 + c // half) * half * half
        r %= half
        c %= half
        n -= 1
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1 0 0\n", "1 1 1\n", "2 3 1\n", "3 7 7\n", "4 8 9\n", "10 512 513\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
