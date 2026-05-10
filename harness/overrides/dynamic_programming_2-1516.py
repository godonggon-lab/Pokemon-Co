from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n10 -1\n", "10\n"),
        edge("3\n10 -1\n20 1 -1\n30 2 -1\n", "10\n30\n60\n"),
        edge("4\n10 -1\n20 -1\n5 1 2 -1\n7 3 -1\n", "10\n20\n25\n32\n"),
        edge("5\n10 -1\n10 1 -1\n4 1 -1\n4 3 1 -1\n3 3 -1\n", "10\n20\n14\n18\n17\n"),
        edge("5\n5 -1\n5 -1\n5 -1\n5 -1\n5 -1\n", "5\n5\n5\n5\n5\n"),
        stress("6\n3 -1\n4 1 -1\n5 1 -1\n6 2 3 -1\n7 4 -1\n8 4 -1\n", "3\n7\n8\n14\n21\n22\n"),
    ]
