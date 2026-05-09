from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n10\n"),
        edge("2\n10 20\n"),
        edge("3\n2 3 6\n"),
        edge("5\n1 1 1 1 100\n"),
        edge("5\n100 1 1 1 1\n"),
        stress("20\n" + " ".join(str(i * 3 + 1) for i in range(20)) + "\n"),
    ]
