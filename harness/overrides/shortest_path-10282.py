from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 0 1\n"),
        edge("1\n2 1 1\n2 1 5\n"),
        edge("1\n3 2 1\n2 1 5\n3 2 7\n"),
        edge("1\n3 1 1\n3 2 7\n"),
        edge("2\n3 2 1\n2 1 5\n3 2 7\n4 3 2\n2 1 2\n3 2 2\n4 3 2\n"),
        stress("1\n6 7 1\n2 1 2\n3 1 4\n4 2 3\n4 3 1\n5 4 5\n6 5 1\n6 3 20\n"),
    ]
