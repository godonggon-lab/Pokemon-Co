from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 5\n", "0\n"),
        edge("5 10\n", "0\n"),
        edge("10 5\n", "5\n"),
        edge("5 17\n", "2\n"),
        edge("1 1024\n", "0\n"),
        stress("99999 100000\n", "1\n"),
    ]
