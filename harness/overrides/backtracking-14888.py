from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _trunc_div(a: int, b: int) -> int:
    return a // b if a >= 0 else -((-a) // b)


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    ops = list(map(int, lines[2].split()))
    mn = 10**18
    mx = -10**18

    def dfs(idx: int, current: int) -> None:
        nonlocal mn, mx
        if idx == n:
            mn = min(mn, current)
            mx = max(mx, current)
            return
        value = nums[idx]
        if ops[0]:
            ops[0] -= 1; dfs(idx + 1, current + value); ops[0] += 1
        if ops[1]:
            ops[1] -= 1; dfs(idx + 1, current - value); ops[1] += 1
        if ops[2]:
            ops[2] -= 1; dfs(idx + 1, current * value); ops[2] += 1
        if ops[3]:
            ops[3] -= 1; dfs(idx + 1, _trunc_div(current, value)); ops[3] += 1

    dfs(1, nums[0])
    return f"{mx}\n{mn}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n5 6\n0 0 1 0\n"),
        edge("6\n1 2 3 4 5 6\n2 1 1 1\n"),
        stress("8\n-3 4 -5 6 -7 8 -9 10\n2 2 2 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
