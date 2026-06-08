from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    target, _ = map(int, lines[0].split())
    lengths = list(map(int, lines[1].split()))
    low, high = 1, max(lengths)
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if sum(length // mid for length in lengths) >= target:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n10\n"),
        edge("2 1\n10\n"),
        edge("3 10\n1 2 3 4 5 6 7 8 9 10\n"),
        edge("5 3\n5 5 5\n"),
        edge("100 2\n1 1\n"),
        stress("100 20\n" + " ".join(str((i*19)%1000+1) for i in range(20)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
