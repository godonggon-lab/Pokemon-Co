from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n0\n"),
        edge("1 1\n1\n"),
        edge("3 3\n1 1 0\n0 1 0\n1 0 1\n"),
        edge("4 5\n1 1 0 0 0\n1 0 0 1 1\n0 0 1 1 1\n1 0 0 0 0\n"),
        stress("10 10\n" + "\n".join(" ".join(str((r + c) % 2) for c in range(10)) for r in range(10)) + "\n"),
    ]
