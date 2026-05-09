from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n", "1\n"),
        edge("1\n2\n", "2\n"),
        edge("1\n3\n", "3\n"),
        edge("1\n4\n", "4\n"),
        edge("5\n1\n2\n3\n4\n10\n", "1\n2\n3\n4\n14\n"),
        edge("3\n6\n7\n8\n", "7\n8\n10\n"),
    ]
