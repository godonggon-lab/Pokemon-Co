from __future__ import annotations

from itertools import product
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    n, m = nums[0], nums[1]
    values = sorted(nums[2 : 2 + n])
    out = []
    for seq in product(values, repeat=m):
        if all(seq[i] <= seq[i + 1] for i in range(m - 1)):
            out.append(" ".join(map(str, seq)))
    return "\n".join(out) + ("\n" if out else "")


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1 1\n7\n",
        "2 1\n2 1\n",
        "2 2\n1 2\n",
        "3 2\n4 2 9\n",
        "4 3\n9 7 1 3\n",
        "5 2\n5 4 3 2 1\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "6 4\n1 3 5 7 9 11\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
