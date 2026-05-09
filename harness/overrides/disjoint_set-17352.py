from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n = nums[0]
    parent = list(range(n + 1))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(1, len(nums), 2):
        a, b = nums[i], nums[i + 1]
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    root = find(1)
    for i in range(2, n + 1):
        if find(i) != root:
            return f"1 {i}\n"
    return ""


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["2\n", "3\n1 2\n", "4\n1 2\n3 4\n", "5\n1 2\n2 3\n4 5\n", "6\n1 2\n2 3\n3 4\n5 6\n", "7\n1 2\n2 3\n4 5\n5 6\n6 7\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
