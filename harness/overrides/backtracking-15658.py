from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _trunc_div(a: int, b: int) -> int:
    return a // b if a >= 0 else -((-a) // b)


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    values = list(map(int, lines[1].split()))
    ops = list(map(int, lines[2].split()))
    mn = 10**18
    mx = -10**18

    def dfs(idx: int, current: int) -> None:
        nonlocal mn, mx
        if idx == n:
            mn = min(mn, current)
            mx = max(mx, current)
            return
        nxt = values[idx]
        if ops[0]:
            ops[0] -= 1; dfs(idx + 1, current + nxt); ops[0] += 1
        if ops[1]:
            ops[1] -= 1; dfs(idx + 1, current - nxt); ops[1] += 1
        if ops[2]:
            ops[2] -= 1; dfs(idx + 1, current * nxt); ops[2] += 1
        if ops[3]:
            ops[3] -= 1; dfs(idx + 1, _trunc_div(current, nxt)); ops[3] += 1

    dfs(1, values[0])
    return f"{mx}\n{mn}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n5 6\n1 0 0 0\n"),
        edge("2\n5 6\n0 1 0 0\n"),
        edge("3\n3 4 5\n1 1 0 0\n"),
        edge("3\n7 3 2\n0 0 1 1\n"),
        edge("4\n1 2 3 4\n1 1 1 0\n"),
        stress("6\n10 20 30 40 50 60\n2 1 1 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
