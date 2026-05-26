from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0 0\n20 0\n0 0 10 0\n10 0 20 0\n5 5 6 6\n"),
        edge("1 1\n9 9\n1 2 8 8\n2 1 8 7\n0 0 3 3\n"),
        stress("0 0\n100 100\n0 1 99 100\n1 0 100 99\n40 40 60 60\n"),
    ]
