from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("3\nA\nB\nC\n"), edge("6\nA\nC\nD\nB\nC\nB\n"), stress("100\n" + "\n".join(chr(65 + (i*7)%26) for i in range(100)) + "\n")]
