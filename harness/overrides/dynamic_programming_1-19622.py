from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 2 10\n"),
        edge("2\n1 2 10\n2 3 20\n"),
        edge("3\n1 2 10\n2 3 100\n3 4 10\n"),
        edge("4\n1 2 10\n2 3 20\n3 4 30\n4 5 40\n"),
        edge("5\n1 2 100\n2 3 1\n3 4 100\n4 5 1\n5 6 100\n"),
        stress("10\n" + "\n".join(f"{i} {i + 1} {((i * 13) % 50) + 1}" for i in range(1, 11)) + "\n"),
    ]
