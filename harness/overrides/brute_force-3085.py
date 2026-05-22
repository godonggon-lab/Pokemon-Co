from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    rows = [("CPZY" * 4)[i:i + 8] for i in range(8)]
    return [edge("3\nCCP\nCCP\nPPC\n"), edge("4\nPPPP\nCYZY\nCCPY\nPPCC\n"), edge("5\nYCPZY\nCYZZP\nCCPPP\nYCYZC\nCPPZZ\n"), stress("8\n" + "\n".join(rows) + "\n")]
