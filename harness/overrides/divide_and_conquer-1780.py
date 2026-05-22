from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n"),
        edge("3\n1 1 1\n1 1 1\n1 1 1\n"),
        edge("3\n-1 0 1\n-1 0 1\n-1 0 1\n"),
        stress("9\n" + "\n".join(" ".join(str((r + c) % 3 - 1) for c in range(9)) for r in range(9)) + "\n"),
    ]
