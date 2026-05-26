from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n3\n1 2 2\n2 3 3\n1 3 10\n"),
        edge("4\n5\n1 2 1\n2 3 1\n3 4 1\n1 4 10\n2 4 5\n"),
        stress("5\n6\n1 2 2\n2 5 2\n1 3 5\n3 4 5\n4 5 5\n2 3 1\n"),
    ]
