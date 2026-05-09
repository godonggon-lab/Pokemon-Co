from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0\n", "0\n"),
        edge("1\n", "1\n"),
        edge("2\n", "2\n"),
        edge("4\n", "2\n"),
        edge("15\n", "4\n"),
        stress("1000000000000000000\n", "1000000000\n"),
    ]
