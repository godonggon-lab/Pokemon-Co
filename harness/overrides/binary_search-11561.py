from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    out = []
    for line in lines[1:1 + int(lines[0])]:
        n = int(line)
        low, high = 1, 2_000_000_000
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            if mid * (mid + 1) // 2 <= n:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        out.append(str(answer))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3\n1\n3\n4\n"),
        edge("2\n2\n5\n"),
        edge("2\n100\n1000000000000000000\n"),
        edge("3\n6\n7\n8\n"),
        edge("4\n15\n16\n999\n1000000\n"),
        stress("5\n10\n1000\n999999\n123456789\n9876543210\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
