from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 0\n10\n"),
        edge("1 1\n20\n"),
        edge("3 1\n10 20 30\n"),
        edge("5 3\n13 20 10 25 30\n"),
        edge("5 10\n11 12 13 14 15\n"),
        stress("20 15\n" + " ".join(str(10 + (i % 9) * 10) for i in range(20)) + "\n"),
    ]
