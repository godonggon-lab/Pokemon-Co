from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge(("0 0 0 0 0 0 0 0 0 0\n"*10)),
        edge(("1 1 1 1 1 0 0 0 0 0\n"*5)+("0 0 0 0 0 0 0 0 0 0\n"*5)),
        stress("1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1\n"),
    ]
