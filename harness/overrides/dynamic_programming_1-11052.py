from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5\n"), edge("4\n1 5 6 7\n"), edge("5\n10 9 8 7 6\n"), stress("20\n" + " ".join(str((i * 13) % 100 + 1) for i in range(1, 21)) + "\n")]
