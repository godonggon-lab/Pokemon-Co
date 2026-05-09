from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2\n1 2\n3 4\n", "10\n"),
        edge("2 3\n1 2 3\n4 5 6\n", "30\n"),
        edge("3 2\n1 2\n3 4\n5 6\n", "32\n"),
        edge("3 3\n1 1 1\n1 10 1\n1 1 1\n", "52\n"),
        edge("4 4\n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n", "354\n"),
        stress("5 6\n1 3 5 7 9 11\n2 4 6 8 10 12\n13 15 17 19 21 23\n14 16 18 20 22 24\n25 26 27 28 29 30\n", "1420\n"),
    ]
