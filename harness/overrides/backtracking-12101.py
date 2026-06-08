from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n, k = map(int, stdin.split())
    values: list[str] = []

    def dfs(total: int, parts: list[int]) -> None:
        if total == n:
            values.append("+".join(map(str, parts)))
            return
        if total > n:
            return
        for value in (1, 2, 3):
            dfs(total + value, parts + [value])

    dfs(0, [])
    return values[k - 1] if k <= len(values) else "-1"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1\n"), edge("2 2\n"), edge("3 4\n"), edge("4 6\n"), edge("5 100\n"), stress("10 100\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
