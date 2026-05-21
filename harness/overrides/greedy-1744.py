from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n"),
        edge("3\n1\n2\n3\n"),
        edge("5\n-1\n-2\n-3\n0\n4\n"),
        edge("6\n-5\n-4\n-1\n0\n1\n2\n"),
        edge("5\n-1\n2\n1\n1\n3\n"),
        stress("20\n" + "\n".join(str((i % 9) - 4) for i in range(20)) + "\n"),
    ]
