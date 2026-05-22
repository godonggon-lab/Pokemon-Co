from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3\n1 2 3\n4 5 6\n7 8 9\n5\n"),
        edge("4 4\n1 1 1 1\n1 9 9 1\n1 9 9 1\n1 1 1 1\n5\n"),
        edge("3 4\n10 20 30 40\n50 60 70 80\n90 100 110 120\n60\n"),
        stress("10 10\n" + "\n".join(" ".join(str((r * 13 + c * 7) % 256) for c in range(10)) for r in range(10)) + "\n100\n"),
    ]
