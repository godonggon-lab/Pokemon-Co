from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n", "0\n"),
        edge("2\n1 2\n", "1\n"),
        edge("3\n1 2\n2 3\n", "1\n"),
        edge("4\n1 2\n1 3\n1 4\n", "1\n"),
        edge("4\n1 2\n2 3\n3 4\n", "2\n"),
        stress("7\n1 2\n1 3\n2 4\n2 5\n3 6\n3 7\n", "2\n"),
    ]
