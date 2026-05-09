from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n50 160\n"),
        edge("2\n50 160\n60 170\n"),
        edge("3\n60 170\n60 170\n70 180\n"),
        edge("5\n55 185\n58 183\n88 186\n60 175\n46 155\n"),
        edge("6\n100 100\n90 110\n110 90\n80 80\n120 120\n100 120\n"),
        stress("10\n50 150\n55 155\n60 160\n65 165\n70 170\n75 175\n80 180\n85 185\n90 190\n95 195\n"),
    ]
