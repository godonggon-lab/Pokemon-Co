from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nAB\n"),
        edge("1\nAA\n"),
        edge("2\nABBA\nABAB\n"),
        edge("3\nAABB\nBBAA\nABBA\n"),
        edge("4\nABAB\nAABB\nBBAABB\nAAAABB\n"),
        stress("5\n" + "A" * 20 + "\n" + "B" * 20 + "\n" + "AB" * 10 + "\n" + "AABB" * 5 + "\n" + "BAAB" * 5 + "\n"),
    ]
