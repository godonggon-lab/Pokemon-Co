from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3\n"),
        edge("5 3\n"),
        edge("6 3\n"),
        edge("7 3\n"),
        edge("100 10\n"),
        stress("100000 447\n"),
    ]
