from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("8 8\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\n"),
        edge("8 8\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\n"),
        edge("10 13\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nWWWWWWWWWWBWB\nWWWWWWWWWWBWB\n"),
        stress("9 9\n" + "\n".join("WBWBWBWBW" if i % 2 == 0 else "BWBWBWBWB" for i in range(9)) + "\n"),
    ]
