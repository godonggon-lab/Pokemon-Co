from __future__ import annotations

from itertools import combinations
from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n, m = nums[0], nums[1]
    vals = nums[2:]
    rows = [vals[i * m:(i + 1) * m] for i in range(n)]
    ans = max(sum(max(row[i], row[j], row[k]) for row in rows) for i, j, k in combinations(range(m), 3))
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1 3\n1 2 3\n",
        "2 3\n1 2 3\n3 2 1\n",
        "3 4\n1 2 3 4\n4 3 2 1\n2 4 1 3\n",
        "4 5\n1 5 3 2 4\n5 1 2 3 4\n2 3 5 1 4\n4 2 1 5 3\n",
        "5 3\n1 1 1\n2 2 2\n3 3 3\n4 4 4\n5 5 5\n",
        "6 6\n1 2 3 4 5 6\n6 5 4 3 2 1\n1 3 5 2 4 6\n6 4 2 5 3 1\n2 2 2 9 1 1\n1 8 1 1 8 1\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
