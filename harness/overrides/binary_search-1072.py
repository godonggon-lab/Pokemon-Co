from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("10 8\n"),
        edge("100 80\n"),
        edge("100 99\n"),
        edge("1 0\n"),
        stress("1000000000 470000000\n"),
    ]
