from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0 1\n", "YES\n"),
        edge("2\n0 1\n3 1\n", "YES\n"),
        edge("2\n0 2\n1 1\n", "NO\n"),
        edge("2\n0 3\n5 1\n", "YES\n"),
        edge("3\n0 10\n-5 2\n5 2\n", "YES\n"),
        stress("4\n0 10\n-5 3\n5 3\n1 1\n", "NO\n"),
    ]
