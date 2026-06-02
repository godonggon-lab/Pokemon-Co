from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    heights = list(map(int, lines[1].split()))
    count = [0] * n
    near = [10**9] * n
    stack = []
    for i, height in enumerate(heights):
        while stack and stack[-1][0] <= height:
            stack.pop()
        count[i] += len(stack)
        if stack:
            near[i] = stack[-1][1]
        stack.append((height, i))
    stack = []
    for i in range(n - 1, -1, -1):
        height = heights[i]
        while stack and stack[-1][0] <= height:
            stack.pop()
        count[i] += len(stack)
        if stack and abs(stack[-1][1] - i) < abs(near[i] - i):
            near[i] = stack[-1][1]
        stack.append((height, i))
    out = []
    for i in range(n):
        if count[i]:
            out.append(f"{count[i]} {near[i] + 1}")
        else:
            out.append("0")
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("5\n1 2 3 4 5\n"),
        edge("5\n5 4 3 2 1\n"),
        stress("8\n3 7 1 6 2 5 4 8\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
