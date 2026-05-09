from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n", "1\n"),
        edge("1 3\n111\n", "3\n"),
        edge("3 1\n1\n1\n1\n", "3\n"),
        edge("2 2\n11\n11\n", "3\n"),
        edge("3 3\n111\n001\n111\n", "5\n"),
        stress("4 4\n1111\n0001\n1111\n1000\n", "-1\n"),
    ]
