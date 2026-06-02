from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    budgets = list(map(int, lines[1].split()))
    total_limit = int(lines[2])
    low, high = 0, max(budgets)
    while low <= high:
        mid = (low + high) // 2
        total = sum(min(budget, mid) for budget in budgets)
        if total <= total_limit:
            low = mid + 1
        else:
            high = mid - 1
    return str(high)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n100\n100\n"),
        edge("1\n100\n50\n"),
        edge("3\n10 20 30\n60\n"),
        edge("4\n120 110 140 150\n485\n"),
        edge("5\n70 80 30 40 100\n300\n"),
        stress("6\n100 200 300 400 500 600\n1000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
