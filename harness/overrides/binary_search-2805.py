from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, needed = map(int, lines[0].split())
    trees = list(map(int, lines[1].split()))
    low, high = 0, max(trees)
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        wood = sum(max(0, tree - mid) for tree in trees)
        if wood >= needed:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n1\n"),
        edge("2 1\n1 2\n"),
        edge("4 7\n20 15 10 17\n"),
        edge("5 20\n4 42 40 26 46\n"),
        edge("5 5\n5 5 5 5 5\n"),
        stress("6 30\n10 20 30 40 50 60\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
