from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n0\n"),
        edge("1\n0\n1\n"),
        edge("2\n00\n11\n"),
        edge("3\n000\n010\n"),
        edge("10\n0000000000\n1111111111\n"),
        stress("30\n" + "01" * 15 + "\n" + "10" * 15 + "\n"),
    ]
