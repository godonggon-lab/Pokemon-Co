from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\n1\n2\n", "1\n"),
        edge("3 3\n1\n5\n3\n", "4\n"),
        edge("4 0\n1\n1\n1\n1\n", "0\n"),
        edge("5 7\n1\n10\n20\n30\n40\n", "9\n"),
        edge("6 4\n8\n1\n5\n12\n3\n9\n", "4\n"),
        stress("10 50\n1\n4\n9\n16\n25\n36\n49\n64\n81\n100\n", "51\n"),
    ]
