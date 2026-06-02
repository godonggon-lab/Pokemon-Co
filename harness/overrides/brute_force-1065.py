from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data)
    answer = 0
    for value in range(1, n + 1):
        digits = list(map(int, str(value)))
        if len(digits) <= 2 or digits[1] - digits[0] == digits[2] - digits[1]:
            answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n"),
        edge("99\n"),
        edge("100\n"),
        edge("110\n"),
        edge("210\n"),
        stress("1000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
