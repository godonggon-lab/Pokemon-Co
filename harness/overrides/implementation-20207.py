from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    days = [0] * 367
    for i in range(1, len(nums), 2):
        for d in range(nums[i], nums[i + 1] + 1):
            days[d] += 1
    ans = width = height = 0
    for d in range(1, 367):
        if days[d]:
            width += 1
            height = max(height, days[d])
        else:
            ans += width * height
            width = height = 0
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n1 1\n", "2\n1 2\n3 4\n", "2\n1 3\n2 4\n", "4\n1 10\n2 3\n5 7\n20 30\n", "5\n1 1\n1 1\n2 2\n2 3\n10 10\n", "6\n1 100\n50 150\n151 200\n201 201\n202 250\n300 365\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
