from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0\n"),
        edge("1\n"),
        edge("2\n"),
        edge("3\n"),
        edge("10\n"),
        stress("35\n"),
    ]
