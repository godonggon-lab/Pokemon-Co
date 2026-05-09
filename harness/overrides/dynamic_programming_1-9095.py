from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n"),
        edge("1\n2\n"),
        edge("1\n3\n"),
        edge("3\n4\n5\n6\n"),
        edge("5\n1\n2\n3\n10\n11\n"),
        stress("11\n" + "\n".join(str(i) for i in range(1, 12)) + "\n"),
    ]
