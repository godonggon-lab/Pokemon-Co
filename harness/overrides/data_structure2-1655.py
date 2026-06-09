from __future__ import annotations

import heapq
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    low: list[int] = []
    high: list[int] = []
    out = []
    for line in lines[1:1 + n]:
        value = int(line)
        if len(low) == len(high):
            heapq.heappush(low, -value)
        else:
            heapq.heappush(high, value)
        if high and -low[0] > high[0]:
            a = -heapq.heappop(low)
            b = heapq.heappop(high)
            heapq.heappush(low, -b)
            heapq.heappush(high, a)
        out.append(str(-low[0]))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n5\n"),
        edge("3\n1\n2\n3\n"),
        edge("4\n5\n4\n3\n2\n"),
        edge("7\n1\n5\n2\n10\n-99\n7\n5\n"),
        edge("6\n0\n0\n0\n0\n0\n0\n"),
        stress("30\n" + "\n".join(str((i * 37) % 101 - 50) for i in range(30)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
