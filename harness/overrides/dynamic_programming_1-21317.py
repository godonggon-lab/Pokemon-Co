from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n10\n", "0\n"),
        edge("2\n3 4\n10\n", "3\n"),
        edge("3\n3 5\n4 6\n10\n", "5\n"),
        edge("4\n5 100\n5 100\n5 100\n1\n", "1\n"),
        edge("5\n1 100\n100 1\n1 100\n100 1\n5\n", "6\n"),
        edge("6\n4 9\n5 10\n6 11\n7 12\n8 13\n3\n", "12\n"),
    ]
