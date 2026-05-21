from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n3 10\n"),
        edge("2\n5 5\n1 6\n"),
        edge("3\n3 8\n2 7\n4 10\n"),
        edge("4\n4 20\n10 15\n2 12\n1 11\n"),
        edge("3\n10 5\n1 20\n1 21\n"),
        stress("20\n" + "\n".join(f"{(i % 5) + 1} {100 - i}" for i in range(20)) + "\n"),
    ]
