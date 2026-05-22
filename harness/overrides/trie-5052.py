from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n3\n911\n97625999\n91125426\n"), edge("1\n3\n113\n12340\n123440\n"), edge("2\n2\n1\n12\n3\n12\n34\n56\n"), stress("1\n10\n" + "\n".join(str(100000 + i * 37) for i in range(10)) + "\n")]
