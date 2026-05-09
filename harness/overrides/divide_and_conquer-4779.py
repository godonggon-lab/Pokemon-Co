from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def cantor(n: int) -> str:
    if n == 0:
        return "-"
    prev = cantor(n - 1)
    return prev + " " * len(prev) + prev


def expected(stdin: str) -> str:
    return "".join(cantor(int(line)) + "\n" for line in stdin.strip().splitlines())


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["0\n", "1\n", "2\n", "0\n1\n2\n", "3\n", "0\n1\n2\n3\n4\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(stdin=inputs[-1]))]
