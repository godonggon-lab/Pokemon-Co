from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n123 3 0\n"),
        edge("1\n123 0 0\n"),
        edge("2\n123 1 1\n356 1 0\n"),
        edge("3\n123 1 1\n456 0 0\n178 1 0\n"),
        edge("4\n123 1 1\n124 2 0\n125 2 0\n126 2 0\n"),
        stress("5\n123 1 1\n356 1 0\n327 2 0\n489 0 1\n789 0 0\n"),
    ]
