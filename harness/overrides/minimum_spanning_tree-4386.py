from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n0.0 0.0\n3.0 4.0\n"),
        edge("3\n0.0 0.0\n3.0 0.0\n0.0 4.0\n"),
        edge("4\n0.0 0.0\n0.0 1.0\n1.0 0.0\n1.0 1.0\n"),
        edge("4\n1.0 1.0\n2.0 2.0\n2.0 4.0\n3.0 3.0\n"),
        edge("5\n0.0 0.0\n2.0 0.0\n4.0 0.0\n4.0 3.0\n0.0 3.0\n"),
        stress("6\n0.0 0.0\n1.5 2.0\n3.0 0.0\n4.5 2.0\n6.0 0.0\n3.0 4.0\n"),
    ]
