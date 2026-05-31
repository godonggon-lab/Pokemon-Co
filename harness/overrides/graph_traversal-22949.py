from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nS...\n....\n....\n...E\n"),
        edge("1\nS#..\n.#..\n..#.\n...E\n"),
        stress("1\nS...\n.##.\n....\n...E\n"),
    ]
