from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n10 1\n20 2\n30 3\n"),
        edge("4\n100 0\n90 20\n80 10\n70 5\n"),
        stress("6\n50 10\n50 0\n40 15\n60 5\n30 20\n70 1\n"),
    ]
