from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n, m, budget = nums[0], nums[1], nums[2]
    cost = [0] + nums[3:3 + n]
    parent = list(range(n + 1))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    idx = 3 + n
    for _ in range(m):
        a, b = nums[idx], nums[idx + 1]
        idx += 2
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
            cost[ra] = min(cost[ra], cost[rb])
            cost[rb] = 0
    total = sum(cost[i] for i in range(1, n + 1) if parent[i] == i or cost[i])
    return "Oh no\n" if total > budget else f"{total}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1 0 10\n5\n",
        "2 1 10\n5 7\n1 2\n",
        "3 1 5\n5 7 1\n1 2\n",
        "4 2 6\n5 1 5 1\n1 2\n3 4\n",
        "5 4 3\n10 10 1 10 10\n1 2\n2 3\n4 5\n3 4\n",
        "6 3 9\n3 4 5 6 7 8\n1 2\n3 4\n5 6\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
