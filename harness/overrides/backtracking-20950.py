from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n255 0 0\n0 255 0\n0 0 255\n128 128 128\n"),
        edge("4\n10 20 30\n40 50 60\n70 80 90\n100 110 120\n50 60 70\n"),
        stress("5\n0 0 0\n255 255 255\n120 80 40\n40 80 120\n200 100 50\n100 100 100\n"),
    ]
