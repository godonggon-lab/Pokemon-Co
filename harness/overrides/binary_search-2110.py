from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 2\n1\n10\n", "9\n"),
        edge("3 2\n1\n2\n4\n", "3\n"),
        edge("5 3\n1\n2\n8\n4\n9\n", "3\n"),
        edge("5 5\n1\n2\n3\n4\n5\n", "1\n"),
        edge("6 3\n1\n10\n20\n30\n40\n50\n", "20\n"),
        stress("8 4\n1\n5\n9\n13\n17\n21\n25\n29\n", "8\n"),
    ]
