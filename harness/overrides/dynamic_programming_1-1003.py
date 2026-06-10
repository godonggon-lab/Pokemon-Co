from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    t = int(lines[0])
    nums = [int(line) for line in lines[1:1 + t]]
    max_n = max(nums) if nums else 0
    zero = [0] * (max_n + 2)
    one = [0] * (max_n + 2)
    zero[0], one[1] = 1, 1
    for i in range(2, max_n + 1):
        zero[i] = zero[i - 1] + zero[i - 2]
        one[i] = one[i - 1] + one[i - 2]
    return "\n".join(f"{zero[n]} {one[n]}" for n in nums)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n0\n"),
        edge("1\n1\n"),
        edge("3\n0\n1\n3\n"),
        edge("4\n2\n3\n4\n5\n"),
        edge("5\n2\n5\n10\n20\n40\n"),
        stress("10\n0\n1\n2\n3\n4\n5\n10\n20\n30\n40\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
