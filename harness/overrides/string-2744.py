from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("a\n"),
        edge("Z\n"),
        edge("HelloWorld\n"),
        edge("BaEkJoOn\n"),
        edge("abcXYZ\n"),
        stress("DongJunCodeDex\n"),
    ]
