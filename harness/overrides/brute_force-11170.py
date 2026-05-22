from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n0 0\n"), edge("3\n0 10\n10 20\n100 200\n"), stress("2\n1 1000\n500 5000\n")]
