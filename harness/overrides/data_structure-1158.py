from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n"),
        edge("3 1\n"),
        edge("3 2\n"),
        edge("7 3\n"),
        edge("5 7\n"),
        stress("10 4\n"),
    ]
