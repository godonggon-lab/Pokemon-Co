from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\n-1 -2\n"),
        edge("2 2\n-1 -2\n"),
        edge("5 5\n1 2 3 4 5\n"),
        edge("5 2\n-5 -4 -3 -2 -1\n"),
        edge("10 2\n3 -2 -4 -9 0 3 7 13 8 -3\n"),
        stress("100 10\n" + " ".join(str((i % 17) - 8) for i in range(100)) + "\n"),
    ]
