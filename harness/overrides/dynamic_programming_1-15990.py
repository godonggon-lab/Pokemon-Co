from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n", "1\n"),
        edge("1\n2\n", "1\n"),
        edge("1\n3\n", "3\n"),
        edge("4\n4\n5\n6\n7\n", "3\n4\n8\n9\n"),
        edge("5\n1\n2\n3\n4\n5\n", "1\n1\n3\n3\n4\n"),
        stress("3\n10\n20\n100\n", "27\n928\n183810299\n"),
    ]
