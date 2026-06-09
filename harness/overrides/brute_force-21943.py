from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    _plus, multiply = map(int, lines[2].split())
    group_count = multiply + 1
    answer = 0

    def dfs(index: int, sums: list[int]) -> None:
        nonlocal answer
        if index == n:
            product = 1
            for value in sums:
                product *= value
            answer = max(answer, product)
            return
        for group in range(group_count):
            sums[group] += nums[index]
            dfs(index + 1, sums)
            sums[group] -= nums[index]

    dfs(0, [0] * group_count)
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n1 2\n1 0\n"),
        edge("3\n1 1 1\n1 1\n"),
        edge("4\n1 2 3 4\n2 1\n"),
        edge("4\n0 1 2 3\n1 2\n"),
        edge("5\n10 1 1 1 1\n3 1\n"),
        stress("5\n5 4 3 2 1\n3 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
