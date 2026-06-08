from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _trunc_div(a: int, b: int) -> int:
    return a // b if a >= 0 else -((-a) // b)


def _eval(nums: list[int], ops: list[str]) -> int:
    stack = [nums[0]]
    add_ops: list[str] = []
    for op, value in zip(ops, nums[1:]):
        if op == "*":
            stack[-1] *= value
        elif op == "/":
            stack[-1] = _trunc_div(stack[-1], value)
        else:
            add_ops.append(op)
            stack.append(value)
    result = stack[0]
    for op, value in zip(add_ops, stack[1:]):
        result = result + value if op == "+" else result - value
    return result


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    counts = list(map(int, lines[2].split()))
    symbols = ["+", "-", "*", "/"]
    mn = 10**18
    mx = -10**18

    def dfs(chosen: list[str]) -> None:
        nonlocal mn, mx
        if len(chosen) == n - 1:
            value = _eval(nums, chosen)
            mn = min(mn, value)
            mx = max(mx, value)
            return
        for i, symbol in enumerate(symbols):
            if counts[i]:
                counts[i] -= 1
                chosen.append(symbol)
                dfs(chosen)
                chosen.pop()
                counts[i] += 1

    dfs([])
    return f"{mx}\n{mn}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n5 6\n0 0 1 0\n"),
        edge("2\n5 2\n0 0 0 1\n"),
        edge("3\n1 2 3\n1 1 0 0\n"),
        edge("4\n1 2 3 4\n1 1 1 0\n"),
        edge("4\n8 3 2 5\n0 1 1 1\n"),
        stress("6\n3 8 2 5 7 4\n2 1 1 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
