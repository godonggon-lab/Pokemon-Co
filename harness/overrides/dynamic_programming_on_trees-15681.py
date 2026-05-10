from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 1\n1\n", "1\n"),
        edge("3 1 3\n1 2\n1 3\n1\n2\n3\n", "3\n1\n1\n"),
        edge("4 2 4\n1 2\n2 3\n2 4\n1\n2\n3\n4\n", "1\n4\n1\n1\n"),
        edge("5 3 5\n1 2\n2 3\n3 4\n4 5\n1\n2\n3\n4\n5\n", "1\n2\n5\n2\n1\n"),
        edge("6 1 3\n1 2\n1 3\n2 4\n2 5\n3 6\n1\n2\n3\n", "6\n3\n2\n"),
        stress("7 4 4\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n4\n1\n7\n5\n", "7\n1\n1\n3\n"),
    ]
