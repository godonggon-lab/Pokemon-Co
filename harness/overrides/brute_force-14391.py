from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n7\n"),
        edge("2 3\n123\n456\n"),
        stress("3 3\n912\n345\n678\n"),
    ]
