from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("4 6\na t c i s w\n"),
        edge("3 5\na b c d e\n"),
        edge("2 4\na b c d\n"),
        edge("5 7\na e i b c d f\n"),
        stress("6 10\na b c d e f g h i j\n"),
    ]
