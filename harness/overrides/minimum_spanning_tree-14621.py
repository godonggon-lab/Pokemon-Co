from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\nM W\n1 2 5\n", "5\n"),
        edge("2 1\nM M\n1 2 5\n", "-1\n"),
        edge("3 3\nM W M\n1 2 3\n2 3 4\n1 3 1\n", "7\n"),
        edge("4 4\nM W M W\n1 2 1\n2 3 2\n3 4 3\n1 4 10\n", "6\n"),
        edge("4 2\nM W M W\n1 2 1\n3 4 1\n", "-1\n"),
        edge("5 6\nM W M W M\n1 2 3\n2 3 2\n3 4 4\n4 5 1\n1 4 10\n2 5 7\n", "10\n"),
    ]
