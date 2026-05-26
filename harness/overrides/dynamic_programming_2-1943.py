from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n500 1\n100 5\n1\n10 3\n1\n7 1\n"),
        edge("3\n1 1\n2 1\n3 1\n2\n1 5\n2 1\n1\n5 1\n"),
        stress("4\n1 10\n5 3\n10 2\n25 1\n3\n2 5\n4 2\n8 1\n2\n3 3\n9 1\n"),
    ]
