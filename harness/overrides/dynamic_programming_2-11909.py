from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n5\n"),
        edge("2\n2 1\n1 0\n"),
        edge("2\n1 2\n3 4\n"),
        edge("3\n9 8 7\n6 5 4\n3 2 1\n"),
        edge("3\n1 5 2\n2 4 3\n3 3 9\n"),
        stress("8\n" + "\n".join(" ".join(str((i * 3 + j * 5) % 17 + 1) for j in range(8)) for i in range(8)) + "\n"),
    ]
