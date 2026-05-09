from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n", "1\n"),
        edge("2\n", "0\n"),
        edge("3\n", "0\n"),
        edge("4\n", "2\n"),
        edge("5\n", "10\n"),
        stress("8\n", "92\n"),
    ]
