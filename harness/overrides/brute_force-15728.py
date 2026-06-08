from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, _k, m = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    b = list(map(int, lines[2].split()))
    for _ in range(m):
        products = sorted(x * y for x in a for y in b)
        target = products[-1]
        for index, x in enumerate(a):
            if any(x * y == target for y in b):
                a.pop(index)
                break
    return str(max(x * y for x in a for y in b))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3 3 1\n1 2 3\n4 5 6\n"),
        edge("2 2 1\n1 10\n1 10\n"),
        edge("3 2 2\n-5 -1 2\n3 -4\n"),
        edge("4 3 2\n-1 3 5 7\n2 -4 6\n"),
        edge("4 3 1\n0 1 2 3\n-1 0 1\n"),
        stress("5 4 3\n1 -2 3 -4 5\n10 20 -30 40\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
