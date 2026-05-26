from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n26 40 83\n49 60 57\n13 89 99\n"),
        edge("4\n1 100 100\n100 1 100\n100 100 1\n1 100 100\n"),
        stress("5\n7 3 8\n2 9 4\n6 1 5\n8 7 2\n3 4 6\n"),
    ]
