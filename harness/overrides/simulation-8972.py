from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3\n...\n.I.\nR..\n5\n"),
        edge("4 4\nR...\n.I..\n....\n...R\n5555\n"),
        stress("5 5\nR...R\n.....\n..I..\n.....\nR...R\n55558888\n"),
    ]
