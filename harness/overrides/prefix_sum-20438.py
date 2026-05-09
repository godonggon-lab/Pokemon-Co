from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 0 1 1\n3\n3 3\n", "0\n"),
        edge("3 0 1 2\n3\n3 5\n4 5\n", "2\n2\n"),
        edge("5 1 1 2\n4\n3\n3 7\n4 7\n", "3\n3\n"),
        edge("5 1 1 2\n3\n4\n3 7\n3 3\n", "4\n1\n"),
        edge("8 2 2 3\n4 6\n3 5\n3 10\n4 8\n6 10\n", "4\n4\n3\n"),
        stress("10 2 3 3\n5 9\n3 4 7\n3 12\n4 10\n8 12\n", "4\n3\n3\n"),
    ]
