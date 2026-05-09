from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n7\n", "0\n"),
        edge("1 2\n7 8\n", "0\n"),
        edge("2 1\n7\n8\n", "0\n"),
        edge("2 2\n1 1\n1 1\n", "4\n"),
        edge("2 2\n1 2\n3 4\n", "13\n"),
        edge("2 3\n1 1 1\n1 1 1\n", "8\n"),
    ]
