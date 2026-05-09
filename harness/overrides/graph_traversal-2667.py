from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n", "0\n"),
        edge("1\n1\n", "1\n1\n"),
        edge("2\n10\n01\n", "2\n1\n1\n"),
        edge("3\n111\n101\n111\n", "1\n8\n"),
        edge("5\n11000\n11000\n00100\n00011\n00011\n", "3\n1\n4\n4\n"),
        edge("5\n10101\n01010\n10101\n01010\n10101\n", "13\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n"),
    ]
