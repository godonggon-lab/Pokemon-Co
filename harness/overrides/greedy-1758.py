from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1\n"),
        edge("3\n1\n2\n3\n"),
        edge("5\n10\n10\n10\n10\n10\n"),
        edge("5\n5\n4\n3\n2\n1\n"),
        edge("6\n100\n1\n100\n1\n100\n1\n"),
        stress("10\n10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n"),
    ]
