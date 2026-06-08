from __future__ import annotations
from math import isqrt
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data)

    def prime(value: int) -> bool:
        if value < 2:
            return False
        for divisor in range(2, isqrt(value) + 1):
            if value % divisor == 0:
                return False
        return True

    out = []

    def dfs(value: int, length: int) -> None:
        if length == n:
            out.append(str(value))
            return
        for digit in (1, 3, 7, 9):
            next_value = value * 10 + digit
            if prime(next_value):
                dfs(next_value, length + 1)

    for start in (2, 3, 5, 7):
        dfs(start, 1)
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("2\n"), edge("3\n"), edge("4\n"), edge("5\n"), stress("8\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
