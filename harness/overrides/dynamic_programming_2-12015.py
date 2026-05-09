from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n7\n", "1\n"),
        edge("5\n1 2 3 4 5\n", "5\n"),
        edge("5\n5 4 3 2 1\n", "1\n"),
        edge("6\n10 20 10 30 20 50\n", "4\n"),
        edge("6\n1 1 1 1 1 1\n", "1\n"),
        stress("50\n" + " ".join(str((i * 17) % 101) for i in range(50)) + "\n", "13\n"),
    ]
