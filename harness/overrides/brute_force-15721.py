from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1\n0\n", "0\n"),
        edge("2\n1\n1\n", "1\n"),
        edge("3\n5\n0\n", "2\n"),
        edge("5\n10\n1\n", "4\n"),
        edge("7\n20\n0\n", "1\n"),
        stress("10\n30\n1\n", "9\n"),
    ]
