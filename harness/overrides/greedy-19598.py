from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 2\n"),
        edge("3\n1 3\n2 4\n3 5\n"),
        edge("3\n1 2\n2 3\n3 4\n"),
        edge("4\n1 10\n2 3\n3 4\n4 5\n"),
        edge("5\n5 6\n1 2\n3 4\n2 3\n4 5\n"),
        stress("20\n" + "\n".join(f"{i} {i + 10}" for i in range(1, 21)) + "\n"),
    ]
