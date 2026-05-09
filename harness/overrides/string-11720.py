from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n0\n"),
        edge("1\n9\n"),
        edge("5\n54321\n"),
        edge("10\n0000000000\n"),
        edge("10\n9090909090\n"),
        stress("100\n" + ("1234567890" * 10) + "\n"),
    ]
