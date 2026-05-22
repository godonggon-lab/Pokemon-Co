from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2\n1 1\n3 1\n"), edge("5\n1 1\n5 1\n3 1\n10 2\n20 2\n"), stress("30\n" + "\n".join(f"{i*3} {i%5}" for i in range(30)) + "\n")]
