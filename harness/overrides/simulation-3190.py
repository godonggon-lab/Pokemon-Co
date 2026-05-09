from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n0\n0\n"),
        edge("3\n1\n1 2\n1\n2 D\n"),
        edge("5\n2\n1 2\n1 3\n2\n3 D\n5 L\n"),
        edge("6\n3\n3 4\n2 5\n5 3\n3\n3 D\n15 L\n17 D\n"),
        edge("7\n4\n2 3\n3 4\n4 5\n5 6\n4\n4 D\n8 D\n12 D\n16 D\n"),
        edge("10\n5\n1 5\n2 5\n3 5\n4 5\n5 5\n4\n8 D\n10 D\n12 D\n14 D\n"),
    ]
