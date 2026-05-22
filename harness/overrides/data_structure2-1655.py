from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n5\n"),
        edge("3\n1\n2\n3\n"),
        edge("4\n5\n4\n3\n2\n"),
        edge("7\n1\n5\n2\n10\n-99\n7\n5\n"),
        stress("30\n" + "\n".join(str((i * 37) % 101 - 50) for i in range(30)) + "\n"),
    ]
