from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1.000\n"), edge("3\n0.500\n0.500\n2.000\n"), edge("8\n1.1\n0.7\n1.3\n0.9\n1.4\n0.8\n1.2\n0.6\n"), stress("20\n" + "\n".join(f"{1 + (i%7)/10:.1f}" for i in range(20)) + "\n")]
