from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("A\nA\n"),
        edge("A\nB\n"),
        edge("ABCBDAB\nBDCABA\n"),
        edge("AAAA\nBBBB\n"),
        edge("XMJYAUZ\nMZJAWXU\n"),
        stress(("ABCD" * 25) + "\n" + ("ACBD" * 25) + "\n"),
    ]
