from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 4\nantatica\n"), edge("1 5\nantatica\n"), edge("3 6\nantarctica\nantahellotica\nantacartica\n"), stress("5 7\nantabtica\nantaztica\nantaytica\nantabytica\nantaxyztica\n")]
