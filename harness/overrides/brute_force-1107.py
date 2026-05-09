from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    target, m = nums[0], nums[1]
    broken = set(nums[2:2 + m])
    ans = abs(target - 100)
    for x in range(1_000_000):
        if all(int(ch) not in broken for ch in str(x)):
            ans = min(ans, len(str(x)) + abs(target - x))
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["100\n0\n", "5457\n3\n6 7 8\n", "0\n0\n", "0\n9\n1 2 3 4 5 6 7 8 9\n", "500000\n8\n0 2 3 4 6 7 8 9\n", "999999\n10\n0 1 2 3 4 5 6 7 8 9\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
