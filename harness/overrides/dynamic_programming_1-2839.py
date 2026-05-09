from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3\n", "1\n"),
        edge("4\n", "-1\n"),
        edge("5\n", "1\n"),
        edge("6\n", "2\n"),
        edge("18\n", "4\n"),
        stress("4999\n", "1001\n"),
    ]
