from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    stones = list(map(int, lines[1].split()))

    def can(limit: int) -> bool:
        reachable = [False] * n
        reachable[0] = True
        for i in range(n):
            if not reachable[i]:
                continue
            for j in range(i + 1, n):
                power = (j - i) * (1 + abs(stones[i] - stones[j]))
                if power <= limit:
                    reachable[j] = True
        return reachable[-1]

    low, high = 0, (n - 1) * (1 + max(stones) - min(stones))
    while low < high:
        mid = (low + high) // 2
        if can(mid):
            high = mid
        else:
            low = mid + 1
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n1 3\n"),
        edge("5\n1 4 2 7 3\n"),
        stress("7\n10 1 9 2 8 3 7\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
