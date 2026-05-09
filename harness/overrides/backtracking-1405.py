from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 100 0 0 0\n"),
        edge("1 25 25 25 25\n"),
        edge("2 50 50 0 0\n"),
        edge("3 25 25 25 25\n"),
        edge("5 100 0 0 0\n"),
        stress("10 25 25 25 25\n"),
    ]
