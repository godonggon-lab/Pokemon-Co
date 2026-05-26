from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 3 1\n10 100\n20 200\n3 10\n3 11\n3 15\n"),
        edge("2 4 3\n10 100\n20 200\n3 15\n2 12 120\n3 10\n3 12\n"),
        stress("3 6 2\n5 50\n10 100\n20 200\n3 7\n1 8 80\n3 9\n2 19 190\n3 20\n3 14\n"),
    ]
