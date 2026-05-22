from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("1\n0\n"), edge("1\n3\nhat headgear\nsunglasses eyewear\nturban headgear\n"), edge("2\n2\na x\nb x\n3\na x\nb y\nc z\n"), stress("1\n10\n" + "\n".join(f"item{i} kind{i%3}" for i in range(10)) + "\n")]
