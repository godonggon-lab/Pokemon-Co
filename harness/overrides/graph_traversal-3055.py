from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 2\nSD\n"), edge("3 3\nS..\n.*.\n..D\n"), stress("4 5\nS....\n.XXX.\n.*...\n...D.\n")]
