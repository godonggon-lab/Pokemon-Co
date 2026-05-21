from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n"),
        edge("1\n1\n"),
        edge("3\n0\n1\n3\n"),
        edge("5\n2\n5\n10\n20\n40\n"),
        stress("10\n0\n1\n2\n3\n4\n5\n10\n20\n30\n40\n"),
    ]
