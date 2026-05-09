from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n"),
        edge("2 1\n1 2\n"),
        edge("4 7\n20 15 10 17\n"),
        edge("5 20\n4 42 40 26 46\n"),
        edge("5 5\n5 5 5 5 5\n"),
        stress("6 30\n10 20 30 40 50 60\n"),
    ]
