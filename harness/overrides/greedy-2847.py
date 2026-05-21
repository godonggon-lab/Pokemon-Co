from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n10\n"),
        edge("3\n1\n2\n3\n"),
        edge("3\n5\n5\n5\n"),
        edge("4\n10\n9\n8\n7\n"),
        edge("5\n10\n20\n20\n30\n30\n"),
        stress("20\n" + "\n".join(str(100 - i // 2) for i in range(20)) + "\n"),
    ]
