from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n"),
        edge("1\n3\n"),
        edge("1\n4\n"),
        edge("3\n5\n6\n7\n"),
        edge("5\n1\n2\n3\n10\n20\n"),
        stress("6\n30\n40\n50\n60\n70\n100\n"),
    ]
