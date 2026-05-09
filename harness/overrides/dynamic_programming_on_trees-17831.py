from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1\n10 20\n"),
        edge("3\n1 1\n10 20 30\n"),
        edge("3\n1 2\n10 20 30\n"),
        edge("5\n1 1 2 2\n3 5 7 11 13\n"),
        edge("6\n1 1 2 2 3\n9 1 8 2 7 3\n"),
        stress("10\n1 1 2 2 3 3 4 4 5\n" + " ".join(str(i * 3 + 1) for i in range(10)) + "\n"),
    ]
