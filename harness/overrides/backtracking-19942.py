from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n10 10 10 10\n10 0 0 0 5\n0 10 0 0 6\n0 0 10 10 7\n"),
        edge("4\n5 5 5 5\n5 5 0 0 10\n0 0 5 5 8\n3 3 3 3 6\n10 10 10 10 50\n"),
        stress("5\n15 15 15 15\n10 5 5 5 10\n5 10 5 5 10\n5 5 10 5 10\n5 5 5 10 10\n20 20 20 20 100\n"),
    ]
