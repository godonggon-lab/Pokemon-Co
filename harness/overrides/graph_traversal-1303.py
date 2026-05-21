from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\nW\n"),
        edge("5 5\nWBWWW\nWWWWW\nBBBBB\nBBBWW\nWWWWW\n"),
        edge("3 2\nWWW\nBBB\n"),
        edge("4 3\nWBWB\nBWBW\nWBWB\n"),
        stress("10 10\n" + "\n".join("W" * 10 if i < 5 else "B" * 10 for i in range(10)) + "\n"),
    ]
