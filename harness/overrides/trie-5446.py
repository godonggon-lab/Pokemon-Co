from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n2\nabc\nabd\n0\n"),
        edge("1\n3\nabc\nabd\nxyz\n1\nabz\n"),
        stress("1\n5\naaa\naab\naba\nbbb\nbbc\n2\naac\nbbd\n"),
    ]
