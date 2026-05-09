from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n2\n", "1 1\n"),
        edge("1\n3\n", "7 7\n"),
        edge("1\n4\n", "4 11\n"),
        edge("1\n5\n", "2 71\n"),
        edge("4\n6\n7\n8\n10\n", "6 111\n8 711\n10 1111\n22 11111\n"),
        stress("3\n15\n20\n30\n", "108 7111111\n688 1111111111\n18888 111111111111111\n"),
    ]
