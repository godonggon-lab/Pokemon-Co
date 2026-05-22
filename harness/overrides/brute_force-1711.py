from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\n0 0\n1 0\n0 1\n"), edge("4\n0 0\n1 0\n0 1\n1 1\n"), edge("5\n0 0\n2 0\n0 2\n2 2\n1 1\n"), stress("8\n" + "\n".join(f"{i%4} {i//4}" for i in range(8)) + "\n")]
