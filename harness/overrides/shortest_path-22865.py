from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("4\n1 2 3\n4\n1 4 5\n2 4 4\n3 4 3\n1 2 1\n"),
        edge("5\n1 3 5\n5\n1 2 2\n2 3 2\n3 4 2\n4 5 2\n2 5 10\n"),
        stress("6\n1 2 6\n7\n1 3 4\n2 3 3\n3 4 2\n4 5 2\n5 6 2\n1 6 10\n2 5 7\n"),
    ]
