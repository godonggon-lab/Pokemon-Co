from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 5\na\nb\n"),
        edge("3 10\nA\nb\nC\n"),
        edge("4 20\nhello\nWorld\nabc\nDef\n"),
        edge("3 12\naa\nbb\ncc\n"),
        stress("5 30\nAlpha\nbeta\nGamma\ndelta\nEpsilon\n"),
    ]
