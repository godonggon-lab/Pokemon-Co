from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5\n1\n2\n3\n4\n5\n"),
        edge("5\n5\n4\n3\n2\n1\n"),
        stress("7\n3\n1\n5\n2\n6\n4\n7\n"),
    ]
