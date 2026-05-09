from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


SOLVED = (
    "1 2 3 4 5 6 7 8 9\n"
    "4 5 6 7 8 9 1 2 3\n"
    "7 8 9 1 2 3 4 5 6\n"
    "2 3 4 5 6 7 8 9 1\n"
    "5 6 7 8 9 1 2 3 4\n"
    "8 9 1 2 3 4 5 6 7\n"
    "3 4 5 6 7 8 9 1 2\n"
    "6 7 8 9 1 2 3 4 5\n"
    "9 1 2 3 4 5 6 7 8\n"
)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge(SOLVED, SOLVED),
        edge(SOLVED.replace("1 2 3", "0 2 3", 1), SOLVED),
        edge(SOLVED.replace("7 8 9", "7 0 9", 1), SOLVED),
        edge(SOLVED.replace("9 1 2", "9 1 0", 1), SOLVED),
        edge(SOLVED.replace("5 6 7", "0 0 7", 1), SOLVED),
        stress(SOLVED.replace("1 2 3 4 5 6 7 8 9", "0 0 0 4 5 6 7 8 9", 1), SOLVED),
    ]
