from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n1 1\n"),
        edge("1\n5\n1 5\n2 4\n3 3\n4 2\n5 1\n"),
        edge("1\n5\n1 1\n2 2\n3 3\n4 4\n5 5\n"),
        edge("2\n3\n1 3\n2 1\n3 2\n4\n4 1\n3 2\n2 3\n1 4\n"),
        stress("1\n20\n" + "\n".join(f"{i} {21 - i}" for i in range(1, 21)) + "\n"),
    ]
