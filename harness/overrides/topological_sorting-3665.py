from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n3\n3 2 1\n0\n"),
        edge("1\n5\n5 4 3 2 1\n2\n2 4\n3 4\n"),
        stress("2\n4\n1 2 3 4\n1\n1 2\n3\n1 2 3\n3\n1 2\n2 3\n1 3\n"),
    ]
