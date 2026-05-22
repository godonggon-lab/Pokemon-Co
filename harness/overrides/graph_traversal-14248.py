from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1\n1\n"), edge("5\n1 2 1 2 1\n3\n"), edge("5\n10 10 10 10 10\n1\n"), stress("30\n" + " ".join(str(i % 5 + 1) for i in range(30)) + "\n15\n")]
