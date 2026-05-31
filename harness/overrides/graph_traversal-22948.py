from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n1 0 10\n2 0 5\n3 0 2\n2 3\n"),
        edge("4\n1 0 20\n2 -5 5\n3 5 5\n4 0 1\n2 3\n"),
        stress("5\n1 0 30\n2 -10 8\n3 10 8\n4 -10 2\n5 10 2\n4 5\n"),
    ]
