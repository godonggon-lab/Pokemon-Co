from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 1 1\n1\n1 1 E\n1 1\n", "1\nS\n"),
        edge("1 2 1\n2 1\n1 1 E\n1 2\n", "2\nF S\n"),
        edge("2 1 1\n2\n1\n1 1 S\n2 1\n", "2\nF\nS\n"),
        edge("2 2 2\n1 1\n1 1\n1 1 E\n1 1\n1 2 S\n2 2\n", "2\nS F\nS S\n"),
        edge("1 3 2\n2 1 1\n1 1 E\n1 3\n1 2 W\n1 2\n", "2\nF S S\n"),
        edge("2 3 1\n3 1 1\n1 1 1\n1 1 E\n2 3\n", "3\nF F F\nS S S\n"),
    ]
