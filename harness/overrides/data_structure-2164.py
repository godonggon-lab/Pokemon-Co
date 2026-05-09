from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n", "1\n"),
        edge("2\n", "2\n"),
        edge("3\n", "2\n"),
        edge("6\n", "4\n"),
        edge("10\n", "4\n"),
        stress("100\n", "72\n"),
    ]
