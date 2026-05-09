from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n7\n"),
        edge("2 1\n2 1\n"),
        edge("2 2\n1 2\n"),
        edge("3 2\n4 2 9\n"),
        edge("4 3\n9 7 1 3\n"),
        edge("5 2\n5 4 3 2 1\n"),
    ]
