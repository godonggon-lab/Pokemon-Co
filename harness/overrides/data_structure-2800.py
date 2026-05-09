from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("(a)\n"),
        edge("(a+b)\n"),
        edge("((a))\n"),
        edge("(a+(b))\n"),
        edge("((a+b)*(c+d))\n"),
        edge("((1+2)*(3+(4*5)))\n"),
    ]
