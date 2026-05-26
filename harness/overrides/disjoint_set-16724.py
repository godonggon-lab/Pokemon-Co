from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\nU\n"), edge("2 2\nRD\nUL\n"), stress("3 4\nRRRD\nULLD\nUUUL\n")]
