from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _calc(a: int, op: str, b: int) -> int:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    return a * b


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    expr = lines[1].strip()
    nums = [int(expr[i]) for i in range(0, n, 2)]
    ops = [expr[i] for i in range(1, n, 2)]
    answer = -10**18

    def dfs(index: int, value: int) -> None:
        nonlocal answer
        if index == len(ops):
            answer = max(answer, value)
            return
        dfs(index + 1, _calc(value, ops[index], nums[index + 1]))
        if index + 1 < len(ops):
            grouped = _calc(nums[index + 1], ops[index + 1], nums[index + 2])
            dfs(index + 2, _calc(value, ops[index], grouped))

    dfs(0, nums[0])
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n7\n"),
        edge("3\n1+2\n"),
        edge("5\n1+2*3\n"),
        edge("9\n3+8*7-9*2\n"),
        edge("7\n8*3-2+1\n"),
        stress("11\n1-2*3+4*5-6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
