from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n"),
        edge("2\n1 2\n"),
        stress("3\n1 2 3\n"),
    ]
