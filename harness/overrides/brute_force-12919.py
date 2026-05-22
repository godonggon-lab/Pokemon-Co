from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("A\nBABA\n"), edge("AB\nABB\n"), edge("A\nABBA\n"), stress("AB\nABBABAABAB\n")]
