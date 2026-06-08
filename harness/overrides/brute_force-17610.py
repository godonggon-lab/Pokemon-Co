from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    weights = list(map(int, lines[1].split()))
    possible = {0}
    for weight in weights:
        nxt = set(possible)
        for value in possible:
            nxt.add(value + weight)
            nxt.add(abs(value - weight))
        possible = nxt
    return str(sum(1 for value in range(1, sum(weights) + 1) if value not in possible))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1\n"),
        edge("1\n5\n"),
        edge("2\n1 4\n"),
        edge("3\n1 2 3\n"),
        edge("4\n2 4 8 16\n"),
        stress("5\n1 3 9 27 81\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
