from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n", "0\n"),
        edge("2\n", "1\n"),
        edge("3\n", "1\n"),
        edge("10\n", "3\n"),
        edge("100\n", "7\n"),
        stress("1000000\n", "19\n"),
    ]
