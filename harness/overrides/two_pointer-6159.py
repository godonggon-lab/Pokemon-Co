from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 10\n4\n6\n"), edge("4 10\n1\n2\n8\n9\n"), edge("5 5\n5\n5\n5\n1\n1\n"), stress("30 50\n" + "\n".join(str((i * 7) % 60 + 1) for i in range(30)) + "\n")]
