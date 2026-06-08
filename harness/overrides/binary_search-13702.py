from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, target = map(int, lines[0].split())
    amounts = list(map(int, lines[1:]))
    low, high = 0, max(amounts)
    while low < high:
        mid = (low + high + 1) // 2
        if mid and sum(amount // mid for amount in amounts) >= target:
            low = mid
        else:
            high = mid - 1
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n10\n"),
        edge("1 2\n10\n"),
        edge("3 5\n10\n10\n10\n"),
        edge("2 100\n1\n1\n"),
        edge("4 4\n1\n2\n3\n4\n"),
        stress("20 100\n" + "\n".join(str((i * 37) % 1000 + 1) for i in range(20)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
