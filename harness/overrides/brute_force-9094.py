from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n2 1\n"),
        edge("1\n5 1\n"),
        edge("2\n10 1\n10 2\n"),
        edge("3\n20 3\n30 4\n40 5\n"),
        edge("4\n5 1\n10 10\n50 7\n70 9\n"),
        stress("5\n100 1\n100 10\n100 50\n99 33\n75 12\n"),
    ]
