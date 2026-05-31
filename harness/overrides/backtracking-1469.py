from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    nums = sorted(map(int, lines[1].split()))
    arr = [-1] * (2 * n)
    answer: list[int] | None = None

    def dfs(idx: int) -> None:
        nonlocal answer
        if answer is not None:
            return
        if idx == n:
            answer = arr[:]
            return
        value = nums[idx]
        for left in range(2 * n - value - 1):
            right = left + value + 1
            if arr[left] == -1 and arr[right] == -1:
                arr[left] = arr[right] = value
                dfs(idx + 1)
                arr[left] = arr[right] = -1

    dfs(0)
    return "-1" if answer is None else " ".join(map(str, answer))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1\n"),
        edge("2\n1 2\n"),
        stress("3\n1 2 3\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
