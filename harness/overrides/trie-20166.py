from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2 3\nAB\nCD\nA\nAB\nABA\n"),
        stress("3 3 4\nABC\nDEF\nGHI\nADG\nAEI\nABC\nCFI\n"),
    ]
