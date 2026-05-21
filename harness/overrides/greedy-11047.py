from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n"),
        edge("3 14\n1\n5\n10\n"),
        edge("4 0\n1\n5\n10\n50\n"),
        edge("5 4790\n1\n10\n100\n1000\n5000\n"),
        edge("6 999\n1\n3\n9\n27\n81\n243\n"),
        stress("10 42000\n1\n5\n10\n50\n100\n500\n1000\n5000\n10000\n50000\n"),
    ]
