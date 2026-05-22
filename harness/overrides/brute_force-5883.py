from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n5\n"), edge("5\n1\n2\n1\n1\n2\n"), edge("7\n1\n2\n2\n1\n2\n2\n1\n"), stress("30\n" + "\n".join(str((i // 3) % 4) for i in range(30)) + "\n")]
