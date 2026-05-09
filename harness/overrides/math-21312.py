from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 2 3\n"),
        edge("2 4 6\n"),
        edge("1 1 1\n"),
        edge("2 3 4\n"),
        edge("9 8 7\n"),
        stress("100 101 102\n"),
    ]
