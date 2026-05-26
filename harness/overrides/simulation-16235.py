from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 1\n1\n1 1 1\n"),
        edge("3 2 3\n1 1 1\n1 1 1\n1 1 1\n1 1 1\n2 2 2\n"),
        stress("4 4 5\n2 3 2 3\n3 2 3 2\n2 3 2 3\n3 2 3 2\n1 1 1\n1 4 2\n4 1 3\n4 4 4\n"),
    ]
