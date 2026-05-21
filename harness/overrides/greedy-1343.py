from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("XXXXXX\n"),
        edge("XX.XX\n"),
        edge("X\n"),
        edge("XXXX.XX.XXXXXX\n"),
        edge("....\n"),
        stress("XXXXXXXXXX.XX.XXXX.XXXXXXXXXXXX\n"),
    ]
