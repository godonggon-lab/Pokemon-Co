from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 2\n23\n"), edge("2 2\n21\n10\n"), stress("4 5\n20000\n11110\n00030\n01110\n")]
