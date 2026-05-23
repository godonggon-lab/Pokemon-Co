from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("5\n"), edge("5\n3\n7\n"), stress("50\n30\n24\n5\n28\n45\n98\n52\n60\n")]
