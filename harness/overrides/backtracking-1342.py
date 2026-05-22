from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("a\n"), edge("aa\n"), edge("ab\n"), edge("aabb\n"), stress("aabbccd\n")]
