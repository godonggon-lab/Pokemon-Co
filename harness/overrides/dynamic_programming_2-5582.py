from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("abc\nabc\n"), edge("abc\ndef\n"), stress("ABRACADABRA\nECADADABRBCRDARA\n")]
