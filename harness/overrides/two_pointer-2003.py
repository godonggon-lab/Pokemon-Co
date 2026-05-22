from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n1\n"),
        edge("4 2\n1 1 1 1\n"),
        edge("10 5\n1 2 3 4 2 5 3 1 1 2\n"),
        stress("100 10\n" + " ".join(str(i % 5 + 1) for i in range(100)) + "\n"),
    ]
