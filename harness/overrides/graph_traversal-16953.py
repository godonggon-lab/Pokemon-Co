from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n"),
        edge("1 2\n"),
        edge("1 21\n"),
        edge("2 162\n"),
        edge("4 42\n"),
        stress("100 40021\n"),
    ]
