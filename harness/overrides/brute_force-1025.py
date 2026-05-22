from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\n9\n"), edge("2 2\n12\n34\n"), edge("3 3\n123\n456\n789\n"), stress("4 5\n00144\n62536\n98765\n43210\n")]
