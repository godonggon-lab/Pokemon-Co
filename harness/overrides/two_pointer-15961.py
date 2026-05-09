from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2 1 1\n1\n1\n"),
        edge("4 4 2 4\n1\n2\n3\n4\n"),
        edge("4 4 2 2\n1\n1\n1\n1\n"),
        edge("5 5 3 5\n1\n2\n3\n2\n1\n"),
        edge("8 30 4 30\n7\n9\n7\n30\n2\n7\n9\n25\n"),
        stress("10 10 4 10\n1\n2\n3\n4\n5\n1\n2\n3\n4\n5\n"),
    ]
