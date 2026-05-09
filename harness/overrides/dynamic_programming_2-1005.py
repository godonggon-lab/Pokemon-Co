from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 0\n10\n1\n", "10\n"),
        edge("1\n3 2\n10 20 30\n1 2\n2 3\n3\n", "60\n"),
        edge("1\n4 3\n10 1 100 10\n1 4\n2 4\n3 4\n4\n", "110\n"),
        edge("1\n4 4\n5 10 20 1\n1 2\n1 3\n2 4\n3 4\n4\n", "26\n"),
        edge("2\n1 0\n7\n1\n3 2\n1 2 3\n1 3\n2 3\n3\n", "7\n5\n"),
        stress("1\n6 6\n3 2 7 4 5 6\n1 3\n2 3\n3 4\n3 5\n4 6\n5 6\n6\n", "21\n"),
    ]
