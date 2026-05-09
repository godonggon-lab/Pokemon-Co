from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2\n1 1\n1 -1\n"),
        edge("2\n2 1\n1 -1\n"),
        edge("3\n2 2 1\n1 2 1\n1 1 -1\n"),
        edge("3\n1 1 1\n2 2 1\n1 1 -1\n"),
        edge("4\n2 3 1 1\n1 2 1 1\n1 1 1 1\n1 1 1 -1\n"),
        edge("4\n3 3 3 3\n3 3 3 3\n3 3 3 3\n3 3 3 -1\n"),
    ]
