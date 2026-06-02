from __future__ import annotations

from itertools import permutations
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    k = int(lines[1])
    cards = lines[2:2 + n]
    return str(len({"".join(items) for items in permutations(cards, k)}))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n1\n1\n2\n"),
        edge("3\n2\n1\n2\n3\n"),
        edge("4\n2\n1\n1\n2\n2\n"),
        edge("4\n3\n12\n34\n56\n78\n"),
        edge("5\n2\n0\n00\n000\n1\n11\n"),
        stress("6\n3\n1\n2\n3\n4\n5\n6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
