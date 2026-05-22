from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1 1\nA\n"), edge("2 4\nCAAB\nADCB\n"), stress("3 5\nABCDE\nFGHIJ\nKLMNO\n")]
