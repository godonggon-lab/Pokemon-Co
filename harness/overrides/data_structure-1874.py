from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n", "+\n-\n"),
        edge("3\n1\n2\n3\n", "+\n-\n+\n-\n+\n-\n"),
        edge("3\n3\n2\n1\n", "+\n+\n+\n-\n-\n-\n"),
        edge("3\n2\n1\n3\n", "+\n+\n-\n-\n+\n-\n"),
        edge("3\n2\n3\n1\n", "+\n+\n-\n+\n-\n-\n"),
        stress("5\n1\n2\n5\n3\n4\n", "NO\n"),
    ]
