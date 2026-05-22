from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n0\n"), edge("2\n0a\na0\n"), edge("3\n0a0\na0b\n0b0\n"), stress("4\n0ab0\na0cd\nbc0e\n0de0\n")]
