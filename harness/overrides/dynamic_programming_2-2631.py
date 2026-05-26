from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n"),
        edge("7\n3\n7\n5\n2\n6\n1\n4\n"),
        stress("8\n8\n1\n7\n2\n6\n3\n5\n4\n"),
    ]
