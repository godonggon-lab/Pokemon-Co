from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 1 1 1 1\n"),
        edge("2\n1 2 3 4 2\n2 1 3 4 1\n3 1 2 4 1\n4 1 2 3 1\n"),
        edge("2\n1 2 3 4 2\n2 1 3 4 1\n3 4 2 1 4\n4 3 2 1 3\n"),
        edge("3\n1 2 3 4 5\n2 1 3 4 5\n3 1 2 4 5\n4 1 2 3 5\n5 1 2 3 4\n6 7 8 9 1\n7 6 8 9 1\n8 6 7 9 1\n9 6 7 8 1\n"),
        edge("3\n1 2 3 4 5\n2 3 4 5 6\n3 4 5 6 7\n4 5 6 7 8\n5 6 7 8 9\n6 1 2 3 4\n7 1 2 3 4\n8 1 2 3 4\n9 1 2 3 4\n"),
        stress("3\n9 1 2 3 4\n8 1 2 3 4\n7 1 2 3 4\n6 1 2 3 4\n5 6 7 8 9\n4 5 6 7 8\n3 4 5 6 7\n2 3 4 5 6\n1 2 3 4 5\n"),
    ]
