from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 4\n0 1\n1 2\n2 3\n3 4\n", "1\n"),
        edge("5 3\n0 1\n1 2\n2 3\n", "0\n"),
        edge("5 4\n0 1\n0 2\n0 3\n0 4\n", "0\n"),
        edge("6 5\n0 1\n1 2\n2 3\n3 4\n4 5\n", "1\n"),
        edge("6 4\n0 1\n2 3\n3 4\n4 5\n", "0\n"),
        stress("7 7\n0 1\n1 2\n2 3\n0 4\n4 5\n5 6\n3 6\n", "1\n"),
    ]
