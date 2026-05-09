from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n", "0\n"),
        edge("5\n0\n1\n0\n0\n0\n", "0\n1\n0\n0\n"),
        edge("6\n3\n2\n1\n0\n0\n0\n", "1\n2\n3\n"),
        edge("7\n5\n5\n1\n0\n0\n0\n0\n", "1\n5\n5\n0\n"),
        edge("8\n10\n0\n3\n0\n7\n0\n0\n0\n", "10\n3\n7\n0\n0\n"),
        stress("12\n9\n1\n8\n0\n7\n0\n6\n0\n5\n0\n0\n0\n", "1\n7\n6\n5\n8\n9\n"),
    ]
