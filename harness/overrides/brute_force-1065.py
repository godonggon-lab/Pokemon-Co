from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n"),
        edge("99\n"),
        edge("100\n"),
        edge("110\n"),
        edge("210\n"),
        stress("1000\n"),
    ]
