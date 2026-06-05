from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, k = nums[:2]
    a = nums[2:]
    reachable = [False] * n
    reachable[0] = True
    for i in range(n):
        if not reachable[i]:
            continue
        for j in range(i + 1, n):
            if (j - i) * (1 + abs(a[i] - a[j])) <= k:
                reachable[j] = True
    return "YES\n" if reachable[-1] else "NO\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 1\n1 1\n"),
        edge("2 1\n1 3\n"),
        edge("3 2\n1 2 3\n"),
        edge("4 3\n1 4 2 5\n"),
        edge("5 10\n1 10 1 10 1\n"),
        stress("8 20\n1 3 6 10 15 21 28 36\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
