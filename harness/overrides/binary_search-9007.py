from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n10 1\n1\n2\n3\n4\n"), edge("1\n25 3\n1 2 3\n4 5 6\n7 8 9\n10 11 12\n"), stress("1\n100 10\n" + "\n".join(" ".join(str((r*17+c*7)%50) for c in range(10)) for r in range(4)) + "\n")]
