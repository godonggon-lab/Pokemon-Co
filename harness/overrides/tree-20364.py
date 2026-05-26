from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("7 4\n3\n6\n7\n4\n"),
        edge("10 5\n2\n4\n8\n5\n10\n"),
        stress("31 8\n16\n8\n24\n12\n30\n2\n3\n6\n"),
    ]
