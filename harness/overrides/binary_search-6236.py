from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1\n100\n"),
        edge("2 1\n10\n20\n"),
        edge("2 2\n10\n20\n"),
        edge("5 3\n100\n400\n300\n100\n500\n"),
        edge("7 5\n100\n400\n300\n100\n500\n101\n400\n"),
        stress("10 4\n10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n"),
    ]
