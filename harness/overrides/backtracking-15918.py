from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n, x, y = map(int, data.split())
    fixed = y - x - 1
    if fixed < 1 or fixed > n:
        return "0"
    arr = [0] * (2 * n + 1)
    used = [False] * (n + 1)
    arr[x] = arr[y] = fixed
    used[fixed] = True
    answer = 0

    def dfs(num: int) -> None:
        nonlocal answer
        while num <= n and used[num]:
            num += 1
        if num > n:
            answer += 1
            return
        for i in range(1, 2 * n - num):
            j = i + num + 1
            if j <= 2 * n and arr[i] == 0 and arr[j] == 0:
                arr[i] = arr[j] = num
                used[num] = True
                dfs(num + 1)
                used[num] = False
                arr[i] = arr[j] = 0

    dfs(1)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 1 3\n"),
        edge("3 1 3\n"),
        edge("4 2 5\n"),
        edge("4 1 6\n"),
        edge("5 2 8\n"),
        stress("5 1 6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
