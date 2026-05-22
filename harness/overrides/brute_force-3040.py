from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("7\n8\n10\n13\n15\n19\n20\n23\n25\n"), edge("20\n7\n23\n19\n10\n15\n25\n8\n13\n"), stress("1\n2\n3\n4\n5\n6\n7\n72\n99\n")]
