from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 1\n1\n2\n3\n1\n"),
        edge("4 2\n10\n13\n17\n20\n3\n7\n"),
        stress("5 2\n5\n8\n11\n14\n17\n3\n6\n"),
    ]
