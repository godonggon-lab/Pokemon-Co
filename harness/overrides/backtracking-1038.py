from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0\n"),
        edge("9\n"),
        edge("10\n"),
        edge("18\n"),
        edge("100\n"),
        stress("1023\n"),
    ]
