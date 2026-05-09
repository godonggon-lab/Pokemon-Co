from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1 1 1\n"),
        edge("2 3\n1 1 1\n1 2 1\n2 2 1\n"),
        edge("3 5\n1 1 1\n1 1 2\n3 1\n4 1\n1 2 1\n"),
        edge("3 6\n1 1 20\n3 1\n3 1\n2 1 20\n4 1\n1 3 1\n"),
        edge("5 8\n1 1 1\n1 2 2\n1 3 3\n3 1\n4 2\n2 3 3\n1 4 4\n1 5 5\n"),
        stress("6 10\n1 1 1\n1 1 2\n3 1\n1 2 1\n4 2\n1 3 20\n3 3\n1 4 10\n2 4 10\n1 5 5\n"),
    ]
