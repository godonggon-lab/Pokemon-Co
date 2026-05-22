from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 1\n1 1\n"),
        edge("3 3 3\n1 1\n1 2\n3 3\n"),
        edge("4 5 6\n1 1\n1 2\n2 2\n4 4\n4 5\n3 5\n"),
        stress("10 10 20\n" + "\n".join(f"{i//2+1} {i%10+1}" for i in range(20)) + "\n"),
    ]
