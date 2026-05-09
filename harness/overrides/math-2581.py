from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n", "-1\n"),
        edge("1\n2\n", "2\n2\n"),
        edge("10\n20\n", "60\n11\n"),
        edge("60\n100\n", "620\n61\n"),
        edge("14\n16\n", "-1\n"),
        stress("2\n997\n", "76127\n2\n"),
    ]
