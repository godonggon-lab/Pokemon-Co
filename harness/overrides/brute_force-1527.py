from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 10\n"),
        edge("44 77\n"),
        edge("100 1000\n"),
        edge("4 4\n"),
        stress("1 1000000000\n"),
    ]
