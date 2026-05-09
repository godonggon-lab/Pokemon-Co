from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    a, b, c, limit = map(int, stdin.split())
    tired = work = 0
    for _ in range(24):
        if tired + a <= limit:
            tired += a
            work += b
        else:
            tired = max(0, tired - c)
    return f"{work}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1 1 1 1\n", "10 5 5 10\n", "5 3 2 10\n", "11 10 5 10\n", "2 10 1 5\n", "3 20 4 9\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
