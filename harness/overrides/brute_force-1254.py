from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("abab\n"),
        edge("abacaba\n"),
        edge("a\n"),
        edge("abcd\n"),
        stress("abcdeffedcbaxyz\n"),
    ]
