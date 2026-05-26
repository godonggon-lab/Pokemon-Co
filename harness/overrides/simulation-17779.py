from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5\n1 2 3 4 5\n5 4 3 2 1\n2 3 4 5 6\n6 5 4 3 2\n1 1 1 1 1\n"),
        edge("6\n1 1 1 1 1 1\n2 2 2 2 2 2\n3 3 3 3 3 3\n4 4 4 4 4 4\n5 5 5 5 5 5\n6 6 6 6 6 6\n"),
        stress("7\n7 6 5 4 3 2 1\n1 2 3 4 5 6 7\n7 7 7 7 7 7 7\n1 1 1 1 1 1 1\n3 1 4 1 5 9 2\n2 7 1 8 2 8 1\n6 5 3 5 8 9 7\n"),
    ]
