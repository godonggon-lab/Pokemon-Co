from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("ABC\nBCA\n"), edge("ABC\nDEF\n"), stress("AABBC\nBACAB\n")]
