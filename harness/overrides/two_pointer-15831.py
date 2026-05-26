from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3 0 2\nWWW\n"), edge("5 1 2\nBWWBW\n"), stress("10 2 4\nWBWBWWBBWW\n")]
