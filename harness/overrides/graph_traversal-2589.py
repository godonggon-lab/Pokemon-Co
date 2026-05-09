from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\nL\n"),
        edge("1 3\nLLL\n"),
        edge("2 2\nLL\nLL\n"),
        edge("3 3\nLLL\nWWW\nLLL\n"),
        edge("5 7\nWLLWWWL\nLLLWLLL\nLWLWLWW\nLWLWLLL\nWLLWLWW\n"),
        stress("8 8\n" + "\n".join(["LLLLLLLL", "LWWWWWLL", "LLLLLWLL", "LLWWWLLL", "LLLLLLLL", "LWWWWWWL", "LLLLLLLL", "WWWWLLLW"]) + "\n"),
    ]
