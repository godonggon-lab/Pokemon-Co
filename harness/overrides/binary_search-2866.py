from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress
def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [edge("2 2\nab\ncd\n"), edge("3 2\naa\nbb\naa\n"), stress("4 3\nabc\ndef\nghi\njkl\n")]
