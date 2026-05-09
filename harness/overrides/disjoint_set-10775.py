from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n1\n"),
        edge("2\n2\n1\n1\n"),
        edge("4\n3\n4\n1\n1\n"),
        edge("4\n6\n2\n2\n3\n3\n4\n4\n"),
        edge("5\n5\n5\n4\n3\n2\n1\n"),
        stress("10\n12\n10\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n"),
    ]
