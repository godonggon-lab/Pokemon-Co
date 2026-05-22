from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n0\n"), edge("3 3\n011\n111\n110\n"), stress("5 4\n01010\n11110\n00010\n01110\n")]
