from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, target = map(int, lines[0].split())
    cables = list(map(int, lines[1:]))
    low, high = 1, max(cables)
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if sum(cable // mid for cable in cables) >= target:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n1\n"),
        edge("1 2\n10\n"),
        edge("2 3\n10\n15\n"),
        edge("4 11\n802\n743\n457\n539\n"),
        edge("3 6\n100\n100\n100\n"),
        stress("5 20\n1000\n900\n800\n700\n600\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
