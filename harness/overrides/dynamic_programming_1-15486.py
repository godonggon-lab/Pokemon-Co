from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 10\n", "10\n"),
        edge("1\n2 10\n", "0\n"),
        edge("3\n1 10\n1 20\n1 30\n", "60\n"),
        edge("3\n3 50\n1 10\n1 10\n", "50\n"),
        edge("7\n3 10\n5 20\n1 10\n1 20\n2 15\n4 40\n2 200\n", "45\n"),
        stress("5\n2 10\n2 20\n2 30\n2 40\n1 100\n", "140\n"),
    ]
