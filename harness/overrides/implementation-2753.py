from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n", "0\n"),
        edge("4\n", "1\n"),
        edge("100\n", "0\n"),
        edge("400\n", "1\n"),
        edge("1900\n", "0\n"),
        stress("2000\n", "1\n"),
    ]
