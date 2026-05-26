from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("A\n1\n10 A\n"), edge("ABC\n2\n10 AB\n5 C\n"), stress("DOG\n4\n5 DO\n6 OG\n10 CAT\n3 G\n")]
