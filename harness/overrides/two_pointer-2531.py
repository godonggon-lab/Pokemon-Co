from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 3 1 3\n1\n2\n"), edge("8 30 4 30\n7\n9\n7\n30\n2\n7\n9\n25\n"), edge("5 5 3 4\n1\n2\n3\n2\n1\n"), stress("30 10 5 7\n" + "\n".join(str(i % 10 + 1) for i in range(30)) + "\n")]
