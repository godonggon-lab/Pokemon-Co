from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n1 A\n"), edge("3\n2 A B\n2 A C\n1 D\n"), stress("4\n3 KIWI APPLE BANANA\n2 KIWI APPLE\n3 KIWI ORANGE PEAR\n1 APPLE\n")]
