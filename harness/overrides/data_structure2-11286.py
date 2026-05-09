from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n", "0\n"),
        edge("5\n0\n1\n0\n0\n0\n", "0\n1\n0\n0\n"),
        edge("6\n-1\n1\n0\n0\n0\n0\n", "-1\n1\n0\n0\n"),
        edge("7\n-5\n3\n-3\n0\n0\n0\n0\n", "-3\n3\n-5\n0\n"),
        edge("8\n2\n-2\n1\n-1\n0\n0\n0\n0\n", "-1\n1\n-2\n2\n"),
        stress("10\n10\n-1\n-10\n1\n0\n0\n0\n0\n0\n0\n", "-1\n1\n-10\n10\n0\n0\n"),
    ]
