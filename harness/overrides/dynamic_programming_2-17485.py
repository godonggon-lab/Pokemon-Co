from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2\n1 2\n3 4\n"),
        edge("3 3\n1 100 1\n1 100 1\n1 1 1\n"),
        edge("3 4\n5 8 5 1\n3 2 4 7\n9 1 3 2\n"),
        edge("4 3\n1 2 3\n4 5 6\n7 8 9\n1 1 1\n"),
        edge("5 5\n9 9 9 9 9\n1 9 1 9 1\n9 1 9 1 9\n1 9 1 9 1\n9 9 9 9 9\n"),
        stress("6 6\n" + "\n".join(" ".join(str((i * 5 + j * 7) % 20 + 1) for j in range(6)) for i in range(6)) + "\n"),
    ]
