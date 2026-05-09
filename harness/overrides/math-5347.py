from __future__ import annotations

from math import gcd
from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    out = []
    for i in range(1, len(nums), 2):
        a, b = nums[i], nums[i + 1]
        out.append(str(a * b // gcd(a, b)))
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n1 1\n", "1\n2 3\n", "2\n6 8\n12 18\n", "3\n100 75\n81 27\n17 34\n", "4\n10 20\n21 6\n14 15\n9 28\n", "5\n1000 999\n123 456\n22 33\n7 11\n1024 64\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
