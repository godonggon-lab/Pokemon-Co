from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 0\n"),
        edge("4 2\n4 2\n3 1\n"),
        edge("5 4\n1 2\n1 3\n3 4\n2 5\n"),
        stress("20 19\n" + "\n".join(f"{i} {i+1}" for i in range(1, 20)) + "\n"),
    ]
