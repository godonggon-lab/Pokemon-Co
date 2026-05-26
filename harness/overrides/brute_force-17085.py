from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 2\n##\n"), edge("3 3\n###\n###\n###\n"), stress("5 5\n..#..\n.###.\n#####\n.###.\n..#..\n")]
