from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n7\n"),
        edge("5\n7\n3 8\n8 1 0\n2 7 4 4\n4 5 2 6 5\n"),
        edge("3\n1\n2 3\n4 5 6\n"),
        stress("20\n" + "\n".join(" ".join(str((r * c + c) % 99 + 1) for c in range(1, r + 2)) for r in range(20)) + "\n"),
    ]
