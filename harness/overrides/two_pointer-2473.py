from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n-1 0 2\n"),
        edge("5\n-5 -2 -1 4 10\n"),
        edge("5\n-100 -10 1 2 98\n"),
        edge("6\n-9 -4 -1 3 7 11\n"),
        edge("5\n1 2 3 4 5\n"),
        stress("30\n" + " ".join(str(i * 7 - 100) for i in range(30)) + "\n"),
    ]
