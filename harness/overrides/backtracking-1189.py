from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 1\n.\n", "1\n"),
        edge("2 2 2\n..\n..\n", "0\n"),
        edge("2 2 3\n..\n..\n", "2\n"),
        edge("2 2 3\n.T\n..\n", "0\n"),
        edge("3 3 5\n...\n...\n...\n", "6\n"),
        stress("3 4 6\n....\n.T..\n....\n", "4\n"),
    ]
