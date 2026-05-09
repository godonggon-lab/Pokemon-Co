from __future__ import annotations

from math import gcd
from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    idx = 1
    out = []
    for _ in range(nums[0]):
        n = nums[idx]
        idx += 1
        arr = nums[idx:idx + n]
        idx += n
        out.append(str(sum(gcd(a, b) for i, a in enumerate(arr) for b in arr[i + 1:])))
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n2 1 1\n", "1\n3 10 20 30\n", "2\n3 10 20 30\n4 7 5 12 18\n", "1\n5 1 2 3 4 5\n", "2\n4 100 50 25 75\n3 17 34 51\n", "3\n3 6 10 15\n4 9 27 81 3\n5 2 4 6 8 10\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
