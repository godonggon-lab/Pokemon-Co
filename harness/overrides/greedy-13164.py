from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n100\n"),
        edge("3 1\n1 3 6\n"),
        edge("3 3\n1 3 6\n"),
        edge("5 2\n1 3 6 10 15\n"),
        edge("6 3\n1 2 3 100 101 102\n"),
        stress("10 4\n1 5 9 13 17 21 25 29 33 37\n"),
    ]
