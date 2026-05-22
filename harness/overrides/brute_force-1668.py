from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n10\n"),
        edge("5\n1\n2\n3\n4\n5\n"),
        edge("5\n5\n4\n3\n2\n1\n"),
        edge("5\n1\n3\n2\n5\n4\n"),
        stress("20\n" + "\n".join(str((i * 7) % 11 + 1) for i in range(20)) + "\n"),
    ]
