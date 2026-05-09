from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    ropes = sorted(nums[1:])
    return f"{max(w * (len(ropes) - i) for i, w in enumerate(ropes))}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n10\n", "2\n10\n15\n", "3\n10\n10\n10\n", "5\n1\n2\n3\n4\n5\n", "5\n100\n1\n1\n1\n1\n", "8\n5\n10\n15\n20\n25\n30\n35\n40\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
