from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 1\nC.C\n"),
        edge("3 3\nC..\n.*.\n..C\n"),
        stress("5 5\nC...*\n***.*\n....*\n.****\n....C\n"),
    ]
