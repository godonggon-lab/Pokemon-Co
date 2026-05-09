from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2 1\n1 2\n3 4\n1\n"),
        edge("2 2 2\n1 2\n3 4\n2 1\n"),
        edge("2 3 1\n1 2 3\n4 5 6\n3\n"),
        edge("3 2 1\n1 2\n3 4\n5 6\n4\n"),
        edge("4 4 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n5 6 1 2\n"),
        stress("4 6 6\n1 2 3 4 5 6\n7 8 9 10 11 12\n13 14 15 16 17 18\n19 20 21 22 23 24\n1 2 3 4 5 6\n"),
    ]
