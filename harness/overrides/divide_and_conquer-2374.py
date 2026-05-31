from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n1\n2\n3\n"),
        edge("5\n3\n1\n2\n1\n3\n"),
        stress("6\n1\n2\n3\n3\n2\n6\n"),
    ]
