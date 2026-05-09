from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n, honey = nums[0], nums[1:]
    prefix = [0]
    for value in honey:
        prefix.append(prefix[-1] + value)
    total = prefix[-1]
    ans = 0
    for i in range(1, n - 1):
        ans = max(ans, (total - honey[0] - honey[i]) + (total - prefix[i + 1]))
        ans = max(ans, (total - honey[-1] - honey[i]) + prefix[i])
        ans = max(ans, (prefix[i + 1] - honey[0]) + (total - prefix[i] - honey[-1]))
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["3\n1 2 3\n", "4\n1 2 3 4\n", "5\n10 1 10 1 10\n", "5\n1 10 1 10 1\n", "6\n5 5 5 5 5 5\n", "8\n1 3 5 7 9 11 13 15\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
