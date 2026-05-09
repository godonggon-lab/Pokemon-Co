from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n2\n"),
        edge("3\n1 2 3\n2\n"),
        edge("4\n2 4 6 8\n3\n"),
        edge("5\n5 10 15 20 25\n6\n"),
        edge("6\n7 11 13 17 19 23\n30\n"),
        stress("8\n1 3 5 7 9 11 13 15\n14\n"),
    ]
