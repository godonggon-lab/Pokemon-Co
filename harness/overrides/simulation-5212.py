from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\nX\n"), edge("3 3\nXXX\nXXX\nXXX\n"), edge("5 5\n.....\n.XXX.\n.XXX.\n.XXX.\n.....\n"), stress("8 8\n" + "\n".join("X.X.X.X." if i % 2 else ".X.X.X.X" for i in range(8)) + "\n")]
