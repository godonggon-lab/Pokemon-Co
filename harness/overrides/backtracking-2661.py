from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n = int(data)

    def good(value: str) -> bool:
        for length in range(1, len(value) // 2 + 1):
            if value[-length:] == value[-2 * length:-length]:
                return False
        return True

    def dfs(value: str) -> str | None:
        if len(value) == n:
            return value
        for char in "123":
            next_value = value + char
            if good(next_value):
                result = dfs(next_value)
                if result is not None:
                    return result
        return None

    return dfs("") or ""


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("7\n"), stress("10\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
