from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 1 1\n0 0\n"),
        edge("1\n2 2 2\n0 0\n1 1\n"),
        edge("1\n3 3 3\n0 0\n1 0\n2 0\n"),
        edge("1\n3 3 3\n0 0\n1 1\n2 2\n"),
        edge("2\n5 3 4\n0 0\n1 0\n3 2\n4 2\n4 4 4\n0 0\n0 1\n1 0\n3 3\n"),
        stress("1\n10 8 12\n0 0\n1 0\n2 0\n5 1\n5 2\n6 2\n9 7\n8 7\n7 7\n3 5\n4 5\n4 6\n"),
    ]
