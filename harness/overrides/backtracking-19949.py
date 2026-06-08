from __future__ import annotations

from functools import lru_cache
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    answers = tuple(map(int, data.split()))

    @lru_cache(None)
    def dfs(index: int, prev1: int, prev2: int, score: int) -> int:
        if index == 10:
            return 1 if score >= 5 else 0
        total = 0
        for pick in range(1, 6):
            if pick == prev1 == prev2:
                continue
            total += dfs(index + 1, pick, prev1, score + (pick == answers[index]))
        return total

    return str(dfs(0, 0, 0, 0))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 2 3 4 5 1 2 3 4 5\n"),
        edge("1 1 1 1 1 1 1 1 1 1\n"),
        edge("2 2 2 2 2 2 2 2 2 2\n"),
        edge("5 5 5 5 5 5 5 5 5 5\n"),
        edge("1 2 1 2 1 2 1 2 1 2\n"),
        stress("5 4 3 2 1 5 4 3 2 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
