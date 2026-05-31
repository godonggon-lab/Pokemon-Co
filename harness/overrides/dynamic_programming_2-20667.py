from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("4 8 3\n4 1 1\n4 2 2\n7 1 2\n7 3 3\n"),
        edge("2 10 10\n3 3 1\n4 4 1\n"),
        stress("5 10 12\n4 5 1\n6 4 2\n3 9 3\n10 1 4\n2 8 1\n"),
    ]
