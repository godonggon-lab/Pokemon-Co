from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1\n1\n2\n"),
        edge("3\n2\n1\n2\n3\n"),
        edge("4\n2\n1\n1\n2\n2\n"),
        edge("4\n3\n12\n34\n56\n78\n"),
        edge("5\n2\n0\n00\n000\n1\n11\n"),
        stress("6\n3\n1\n2\n3\n4\n5\n6\n"),
    ]
