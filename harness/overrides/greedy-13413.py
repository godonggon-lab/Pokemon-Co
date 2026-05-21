from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\nB\nW\n"),
        edge("1\n4\nBBBB\nWWWW\n"),
        edge("1\n4\nBWBW\nWBWB\n"),
        edge("2\n5\nBBBBB\nBBBBB\n6\nBWBWBW\nWWBBWB\n"),
        stress("1\n100\n" + "BW" * 50 + "\n" + "WB" * 50 + "\n"),
    ]
