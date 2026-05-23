from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    base = "\n".join(f"{i} {31-i}" for i in range(1, 31)) + "\n"
    return [edge(base), stress("\n".join(f"{(i*7)%100} {(i*11)%100}" for i in range(35)) + "\n")]
