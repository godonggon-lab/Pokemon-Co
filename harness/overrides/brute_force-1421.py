from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 10\n10\n"),
        edge("2 10 1\n10\n20\n"),
        edge("3 1 10\n26\n103\n59\n"),
        edge("4 5 3\n4\n8\n12\n16\n"),
        stress("10 2 7\n" + "\n".join(str((i + 1) * 11) for i in range(10)) + "\n"),
    ]
