from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\nA => B\n"), edge("3\nA => B\nB => C\na => A\n"), stress("5\nA => B\nB => C\nC => D\na => b\nb => C\n")]
