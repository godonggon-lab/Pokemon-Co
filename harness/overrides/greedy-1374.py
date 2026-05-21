from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 1 2\n"),
        edge("3\n1 1 3\n2 2 4\n3 3 5\n"),
        edge("3\n1 1 2\n2 2 3\n3 3 4\n"),
        edge("4\n1 1 10\n2 2 3\n3 3 4\n4 4 5\n"),
        stress("20\n" + "\n".join(f"{i+1} {i%5} {i%5+10}" for i in range(20)) + "\n"),
    ]
