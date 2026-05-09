from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\n1 1\n.\n0\n", "0\n"),
        edge("1\n1 1\n$\n0\n", "1\n"),
        edge("1\n1 2\nA$\na\n", "1\n"),
        edge("1\n1 2\nA$\n0\n", "1\n"),
        edge("1\n3 3\n***\n*$*\n***\n0\n", "0\n"),
        edge("1\n3 5\n*aA$*\n*...*\n*****\n0\n", "1\n"),
    ]
