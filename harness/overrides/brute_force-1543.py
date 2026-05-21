from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("abababa\naba\n"),
        edge("aaaaa\naa\n"),
        edge("abc\nz\n"),
        edge("hellohello\nhello\n"),
        stress(("abc" * 100) + "\nabc\n"),
    ]
