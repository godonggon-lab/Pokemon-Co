from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0 0\n"),
        edge("2\n0 0\n10 10\n"),
        edge("3\n-1 -1\n0 0\n1 1\n"),
        edge("5\n1 10\n2 20\n3 30\n4 40\n5 50\n"),
        edge("4\n100 -100\n-100 100\n100 100\n-100 -100\n"),
        stress("30\n" + "\n".join(f"{i - 15} {(i * i) % 17 - 8}" for i in range(30)) + "\n"),
    ]
