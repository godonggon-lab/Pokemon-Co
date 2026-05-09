from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 0 1\n", "1 \n1 \n"),
        edge("3 2 1\n1 2\n2 3\n", "1 2 3 \n1 2 3 \n"),
        edge("4 4 1\n1 2\n1 3\n2 4\n3 4\n", "1 2 4 3 \n1 2 3 4 \n"),
        edge("4 2 3\n1 2\n3 4\n", "3 4 \n3 4 \n"),
        edge("5 5 2\n1 2\n1 3\n2 4\n3 4\n4 5\n", "2 1 3 4 5 \n2 1 4 3 5 \n"),
        stress("6 7 1\n1 2\n1 3\n2 4\n2 5\n3 5\n4 6\n5 6\n", "1 2 4 6 5 3 \n1 2 3 4 5 6 \n"),
    ]
