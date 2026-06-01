from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, k = map(int, lines[0].split())
    gains = list(map(int, lines[1].split()))
    used = [False] * n
    answer = 0

    def dfs(day: int, weight: int) -> None:
        nonlocal answer
        if day == n:
            answer += 1
            return
        for i in range(n):
            next_weight = weight + gains[i] - k
            if not used[i] and next_weight >= 500:
                used[i] = True
                dfs(day + 1, next_weight)
                used[i] = False

    dfs(0, 500)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 5\n5\n"), edge("3 4\n3 7 5\n"), stress("5 3\n1 2 3 4 5\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
