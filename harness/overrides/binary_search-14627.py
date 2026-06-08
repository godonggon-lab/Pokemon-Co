from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, target = map(int, lines[0].split())
    lengths = list(map(int, lines[1:]))
    low, high = 1, max(lengths)
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if sum(length // mid for length in lengths) >= target:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return str(sum(lengths) - answer * target)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n10\n"),
        edge("1 2\n10\n"),
        edge("3 5\n10\n10\n10\n"),
        edge("2 2\n1\n1\n"),
        edge("4 4\n5\n6\n7\n8\n"),
        stress("20 100\n" + "\n".join(str((i * 31) % 1000 + 10) for i in range(20)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
