from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n5\n"),
        edge("2\n1\n1 10\n"),
        edge("5\n5\n1 3 6 6 7\n"),
        edge("6\n2\n1 2 3 100 101 102\n"),
        edge("8\n3\n1 5 9 13 17 21 25 29\n"),
        stress("10\n4\n1 2 4 8 16 32 64 128 256 512\n"),
    ]
