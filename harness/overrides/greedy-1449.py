from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n5\n"),
        edge("4 2\n1 2 100 101\n"),
        edge("4 3\n1 2 3 4\n"),
        edge("5 4\n10 1 6 2 3\n"),
        edge("6 1\n1 2 3 4 5 6\n"),
        stress("20 5\n" + " ".join(str(i * 3 + 1) for i in range(20)) + "\n"),
    ]
