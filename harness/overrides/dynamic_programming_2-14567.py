from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 0\n"),
        edge("3 0\n"),
        edge("3 2\n1 2\n2 3\n"),
        edge("4 3\n1 3\n2 3\n3 4\n"),
        edge("5 4\n1 2\n1 3\n2 4\n3 5\n"),
        stress("6 6\n1 3\n2 3\n3 4\n3 5\n4 6\n5 6\n"),
    ]
