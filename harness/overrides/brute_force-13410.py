from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n"),
        edge("12 5\n"),
        edge("10 10\n"),
        edge("97 9\n"),
        edge("123 20\n"),
        stress("999 100\n"),
    ]
