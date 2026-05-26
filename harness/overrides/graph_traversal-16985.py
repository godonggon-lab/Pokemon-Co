from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    open_layer = "1 1 1 1 1\n" * 5
    block_layer = "0 0 0 0 0\n" * 5
    return [edge(open_layer*5), edge(block_layer*5), stress((open_layer*4)+("1 1 1 1 1\n1 0 0 0 1\n1 0 1 0 1\n1 0 0 0 1\n1 1 1 1 1\n"))]
