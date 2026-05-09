from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("5 0\n", "1\n"),
        edge("5 5\n", "1\n"),
        edge("5 2\n", "10\n"),
        edge("30 15\n", "155117520\n"),
        edge("100 6\n", "1192052400\n"),
        stress("100 50\n", "100891344545564193334812497256\n"),
    ]
