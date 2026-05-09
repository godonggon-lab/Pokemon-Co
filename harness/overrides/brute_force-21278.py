from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\n1 2\n"),
        edge("3 2\n1 2\n2 3\n"),
        edge("4 3\n1 2\n2 3\n3 4\n"),
        edge("5 4\n1 2\n1 3\n1 4\n1 5\n"),
        edge("5 5\n1 2\n2 3\n3 4\n4 5\n1 5\n"),
        stress("6 7\n1 2\n1 3\n2 4\n3 4\n4 5\n5 6\n2 6\n"),
    ]
