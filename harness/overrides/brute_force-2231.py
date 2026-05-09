from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n", "0\n"),
        edge("10\n", "5\n"),
        edge("216\n", "198\n"),
        edge("100\n", "86\n"),
        edge("999\n", "981\n"),
        stress("1000000\n", "0\n"),
    ]
