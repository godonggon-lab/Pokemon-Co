from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, _count = map(int, lines[0].split())
    digits = list(map(int, lines[1].split()))
    answer = 0

    def backtrack(value: int) -> None:
        nonlocal answer
        if value > n:
            return
        answer = max(answer, value)
        for digit in digits:
            backtrack(value * 10 + digit)

    backtrack(0)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("10 1\n1\n"),
        edge("100 2\n1 9\n"),
        edge("657 3\n1 5 7\n"),
        edge("999 3\n3 6 9\n"),
        edge("1234 4\n1 2 3 4\n"),
        stress("98765 5\n1 3 5 7 9\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
