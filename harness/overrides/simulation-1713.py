from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n3\n1 2 3\n"),
        edge("3\n9\n2 1 4 3 5 6 2 7 2\n"),
        edge("3\n6\n1 1 1 2 2 3\n"),
        edge("2\n7\n1 2 3 2 3 4 4\n"),
        stress("5\n30\n" + " ".join(str(i % 9 + 1) for i in range(30)) + "\n"),
    ]
