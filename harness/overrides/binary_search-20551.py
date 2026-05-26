from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 3\n1\n2\n2\n3\n5\n2\n4\n1\n"),
        edge("1 2\n7\n7\n8\n"),
        stress("8 5\n5\n1\n3\n3\n9\n5\n1\n7\n1\n3\n5\n6\n9\n"),
    ]
