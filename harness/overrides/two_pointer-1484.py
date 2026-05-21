from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n"),
        edge("3\n"),
        edge("15\n"),
        edge("100\n"),
        stress("99999\n"),
    ]
