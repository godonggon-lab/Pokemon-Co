from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("10 2\n3 5\n"),
        edge("7 3\n2 4 6\n"),
        stress("15 4\n1 3 7 10\n"),
    ]
