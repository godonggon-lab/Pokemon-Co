from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nA\n5\n"),
        edge("2\nAB+\n1\n2\n"),
        edge("2\nAB-\n1\n2\n"),
        edge("2\nAB/\n5\n2\n"),
        edge("3\nAB*C+\n2\n3\n4\n"),
        stress("5\nABC*+DE/-\n1\n2\n3\n4\n5\n"),
    ]
