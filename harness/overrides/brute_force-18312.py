from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0 0\n", "3600\n"),
        edge("1 1\n", "5175\n"),
        edge("5 3\n", "11475\n"),
        edge("12 5\n", "22500\n"),
        edge("23 9\n", "22248\n"),
        stress("23 0\n", "62100\n"),
    ]
