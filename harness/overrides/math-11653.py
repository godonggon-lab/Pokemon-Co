from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n"),
        edge("2\n"),
        edge("12\n"),
        edge("999\n"),
        edge("9973\n"),
        stress("100000\n"),
    ]
