from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("()\n", "0\n"),
        edge("(())\n", "2\n"),
        edge("()()\n", "0\n"),
        edge("((()))\n", "4\n"),
        edge("()(((()())(())()))(())\n", "17\n"),
        stress("((()())())\n", "7\n"),
    ]
