from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\nD 1\n", "EMPTY\n"),
        edge("1\n2\nI 5\nD 1\n", "EMPTY\n"),
        edge("1\n3\nI 5\nI 3\nD -1\n", "5 5\n"),
        edge("1\n4\nI 5\nI 3\nD 1\nI 4\n", "4 3\n"),
        edge("1\n5\nI 1\nI 1\nD 1\nI 2\nD -1\n", "2 2\n"),
        stress("2\n4\nI 10\nI 20\nD 1\nD -1\n7\nI 5\nI 3\nI 7\nD -1\nI 9\nD 1\nI 4\n", "EMPTY\n7 4\n"),
    ]
