from __future__ import annotations
from itertools import combinations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    out = []
    for line in data.splitlines():
        numbers = list(map(int, line.split()))
        if numbers[0] == 0:
            break
        for selected in combinations(numbers[1:], 6):
            out.append(" ".join(map(str, selected)))
        out.append("")
    return "\n".join(out).rstrip()


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("6 1 2 3 4 5 6\n0\n"),
        edge("7 1 2 3 4 5 6 7\n0\n"),
        edge("8 1 2 3 4 5 6 7 8\n0\n"),
        edge("6 10 20 30 40 50 60\n0\n"),
        edge("7 3 5 7 11 13 17 19\n0\n"),
        stress("7 1 2 3 4 5 6 7\n8 3 5 7 11 13 17 19 23\n0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
