from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1\n1 2 5\n1 2\n"),
        edge("5\n8\n1 2 2\n1 3 3\n2 3 1\n2 4 5\n3 4 1\n4 5 2\n1 5 20\n3 5 10\n1 5\n"),
        edge("3\n3\n1 2 10\n1 2 1\n2 3 1\n1 3\n"),
        stress("20\n19\n" + "\n".join(f"{i} {i+1} {i}" for i in range(1, 20)) + "\n1 20\n"),
    ]
