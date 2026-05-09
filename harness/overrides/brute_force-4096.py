from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n"),
        edge("9\n0\n"),
        edge("10\n0\n"),
        edge("0990\n0\n"),
        edge("1234\n9999\n0\n"),
        stress("0001\n12932\n808\n0\n"),
    ]
