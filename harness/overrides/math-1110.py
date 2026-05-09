from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0\n", "1\n"),
        edge("1\n", "60\n"),
        edge("26\n", "4\n"),
        edge("55\n", "3\n"),
        edge("71\n", "12\n"),
        stress("99\n", "60\n"),
    ]
