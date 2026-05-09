from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0 1\n", "YES\n"),
        edge("1 2\n", "YES\n"),
        edge("1 3\n", "NO\n"),
        edge("2 4\n", "YES\n"),
        edge("3 6\n", "YES\n"),
        stress("10 30\n", "NO\n"),
    ]
