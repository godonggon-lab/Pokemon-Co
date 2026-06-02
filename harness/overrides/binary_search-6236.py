from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, withdraw_limit = map(int, lines[0].split())
    costs = list(map(int, lines[1:]))
    low, high = max(costs), sum(costs)
    answer = high
    while low <= high:
        mid = (low + high) // 2
        have = count = 0
        for cost in costs:
            if have < cost:
                have = mid - cost
                count += 1
            else:
                have -= cost
        if count > withdraw_limit:
            low = mid + 1
        else:
            answer = mid
            high = mid - 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n100\n"),
        edge("2 1\n10\n20\n"),
        edge("2 2\n10\n20\n"),
        edge("5 3\n100\n400\n300\n100\n500\n"),
        edge("7 5\n100\n400\n300\n100\n500\n101\n400\n"),
        stress("10 4\n10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
