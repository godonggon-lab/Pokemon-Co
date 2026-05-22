from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\nR\n"), edge("5\nRRRBB\nGGBBB\nBBBRR\nBBRRR\nRRRRR\n"), stress("10\n" + "\n".join(("RGB"*4)[:10] for _ in range(10)) + "\n")]
