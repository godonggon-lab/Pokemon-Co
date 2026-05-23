from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\nab\n"), edge("1\naab\n"), stress("2\nabc\naabb\n")]
