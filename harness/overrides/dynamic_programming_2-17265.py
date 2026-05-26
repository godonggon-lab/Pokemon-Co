from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n7\n"), edge("3\n1 + 2\n* 3 -\n4 + 5\n"), stress("5\n1 + 2 * 3\n- 4 + 5 -\n6 * 7 + 8\n+ 9 - 1 *\n2 + 3 - 4\n")]
