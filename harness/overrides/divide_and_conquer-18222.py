from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    k = int(stdin) - 1
    return f"{k.bit_count() % 2}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "2\n", "3\n", "4\n", "10\n", "1000000000000000000\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
