from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("XXXOO.XXX\nend\n"),
        edge("XOXOXOXOX\nend\n"),
        stress(".........\nXXXOOO...\nXXOOOXXOX\nend\n"),
    ]
