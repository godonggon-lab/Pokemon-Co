from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 10\n5\n"),
        edge("2 1 10\n5\n7\n"),
        edge("2 2 10\n5\n7\n"),
        edge("3 2 10\n1\n10\n2\n"),
        edge("5 3 5\n1\n2\n10\n11\n12\n"),
        stress("8 3 7\n1\n3\n6\n10\n15\n21\n28\n36\n"),
    ]
