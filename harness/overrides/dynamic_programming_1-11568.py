from __future__ import annotations
import bisect
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    lis: list[int] = []
    for value in nums[:n]:
        index = bisect.bisect_left(lis, value)
        if index == len(lis):
            lis.append(value)
        else:
            lis[index] = value
    return str(len(lis))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n5\n"),
        edge("5\n1 2 3 4 5\n"),
        edge("5\n5 4 3 2 1\n"),
        edge("5\n3 3 3 3 3\n"),
        edge("7\n1 3 2 4 3 5 4\n"),
        stress("50\n" + " ".join(str((i * 19) % 30) for i in range(50)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
