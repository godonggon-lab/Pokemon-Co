from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    cards = list(range(1, int(stdin) + 1))
    while len(cards) > 1:
        cards = cards[1::2]
    return f"{cards[0]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "2\n", "3\n", "4\n", "10\n", "100\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
