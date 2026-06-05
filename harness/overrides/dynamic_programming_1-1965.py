from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress
import bisect


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    a = nums[1:]
    lis: list[int] = []
    for x in a:
        i = bisect.bisect_left(lis, x)
        if i == len(lis):
            lis.append(x)
        else:
            lis[i] = x
    return f"{len(lis)}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n5\n"),
        edge("5\n1 2 3 4 5\n"),
        edge("5\n5 4 3 2 1\n"),
        edge("8\n1 6 2 5 7 3 5 6\n"),
        stress("50\n" + " ".join(str((i * 17) % 30) for i in range(50)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
