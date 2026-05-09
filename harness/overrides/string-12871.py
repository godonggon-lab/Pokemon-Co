from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("a\na\n"),
        edge("ab\nabab\n"),
        edge("ab\naba\n"),
        edge("abc\nabcabc\n"),
        edge("abab\nab\n"),
        stress("abcab\nabc\n"),
    ]
