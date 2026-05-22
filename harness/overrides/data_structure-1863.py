from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 0\n"),
        edge("4\n1 1\n2 2\n3 1\n4 0\n"),
        edge("5\n1 3\n2 3\n3 2\n4 2\n5 0\n"),
        stress("20\n" + "\n".join(f"{i} {(i * 7) % 5}" for i in range(1, 21)) + "\n"),
    ]
