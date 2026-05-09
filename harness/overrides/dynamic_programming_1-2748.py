from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("0\n", "0\n"),
        edge("1\n", "1\n"),
        edge("2\n", "1\n"),
        edge("10\n", "55\n"),
        edge("50\n", "12586269025\n"),
        stress("90\n", "2880067194370816120\n"),
    ]
