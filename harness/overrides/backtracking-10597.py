from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("123456789\n"),
        edge("123456789101112\n"),
        stress("10987654321\n"),
    ]
