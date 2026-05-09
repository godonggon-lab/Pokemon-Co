from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n"),
        edge("5 11\n1 2 3 4 5\n"),
        edge("5 100\n1 2 3 4 5\n"),
        edge("10 15\n5 1 3 5 10 7 4 9 2 8\n"),
        edge("10 10\n1 1 1 1 10 1 1 1 1 1\n"),
        stress("100 250\n" + " ".join(str((i % 9) + 1) for i in range(100)) + "\n"),
    ]
