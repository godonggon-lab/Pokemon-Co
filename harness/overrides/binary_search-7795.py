from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1 1\n2\n1\n"), edge("2\n5 3\n8 1 7 3 1\n3 6 1\n3 4\n1 1 1\n2 2 2 2\n"), stress("1\n50 50\n" + " ".join(str(i) for i in range(50)) + "\n" + " ".join(str(i*2) for i in range(50)) + "\n")]
