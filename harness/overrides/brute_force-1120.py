from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("adaabc aababbc\n"),
        edge("abc abc\n"),
        edge("abc zzzabczzz\n"),
        edge("aaaa bbbbb\n"),
        stress("abcde " + "x" * 20 + "abzde" + "y" * 20 + "\n"),
    ]
