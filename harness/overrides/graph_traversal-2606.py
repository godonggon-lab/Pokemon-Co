from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n", "0\n"),
        edge("2\n1\n1 2\n", "1\n"),
        edge("4\n2\n1 2\n3 4\n", "1\n"),
        edge("7\n6\n1 2\n2 3\n1 5\n5 2\n5 6\n4 7\n", "4\n"),
        edge("5\n4\n1 2\n2 3\n3 4\n4 5\n", "4\n"),
        stress("6\n3\n2 3\n3 4\n5 6\n", "0\n"),
    ]
