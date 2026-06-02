from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    low, high = map(int, data.split())
    answer = 0

    def dfs(value: int) -> None:
        nonlocal answer
        if value > high:
            return
        if value >= low:
            answer += 1
        dfs(value * 10 + 4)
        dfs(value * 10 + 7)

    dfs(0)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 10\n"),
        edge("44 77\n"),
        edge("100 1000\n"),
        edge("4 4\n"),
        stress("1 1000000000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
