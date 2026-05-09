from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1 2\n", "1\n"),
        edge("3\n1 2\n1 3\n", "1\n1\n"),
        edge("4\n1 2\n2 3\n2 4\n", "1\n2\n2\n"),
        edge("5\n1 3\n3 2\n3 4\n4 5\n", "3\n1\n3\n4\n"),
        edge("7\n1 6\n6 3\n3 5\n4 1\n2 4\n4 7\n", "4\n6\n1\n3\n1\n4\n"),
        stress("8\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n7 8\n", "1\n2\n3\n4\n5\n6\n7\n"),
    ]
