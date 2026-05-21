from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("10 0\n"),
        edge("10 3\n1 2 3\n"),
        edge("100 5\n1 5 10 20 25\n"),
        edge("1 1\n1\n"),
        stress("500 10\n" + " ".join(str(i) for i in range(1, 11)) + "\n"),
    ]
