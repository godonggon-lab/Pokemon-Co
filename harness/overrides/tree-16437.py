from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n"), edge("3\nS 10 1\nW 3 1\n"), stress("6\nS 5 1\nW 10 2\nS 20 2\nW 3 4\nS 7 4\n")]
