from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 0\n"),
        edge("1\n2 1\n1 2\n"),
        edge("1\n3 3\n1 2\n2 3\n3 1\n"),
        edge("1\n4 4\n1 2\n2 3\n3 4\n4 1\n"),
        edge("2\n3 2\n1 2\n2 3\n3 3\n1 2\n2 3\n3 1\n"),
        stress("1\n8 7\n1 2\n2 3\n3 4\n4 5\n5 6\n6 7\n7 8\n"),
    ]
