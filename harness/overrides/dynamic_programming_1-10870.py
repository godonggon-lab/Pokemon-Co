from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0\n", "0\n"),
        edge("1\n", "1\n"),
        edge("2\n", "1\n"),
        edge("10\n", "55\n"),
        edge("19\n", "4181\n"),
        edge("20\n", "6765\n"),
    ]
