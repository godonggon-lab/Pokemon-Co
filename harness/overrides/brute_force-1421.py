from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, cut_cost, price = map(int, lines[0].split())
    logs = list(map(int, lines[1:]))
    answer = 0
    for length in range(1, max(logs) + 1):
        profit = 0
        for log in logs:
            pieces = log // length
            if pieces == 0:
                continue
            cuts = pieces - 1 if log % length == 0 else pieces
            gain = pieces * length * price - cuts * cut_cost
            if gain > 0:
                profit += gain
        answer = max(answer, profit)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1 10\n10\n"),
        edge("2 10 1\n10\n20\n"),
        edge("3 1 10\n26\n103\n59\n"),
        edge("4 5 3\n4\n8\n12\n16\n"),
        edge("2 100 1\n5\n6\n"),
        stress("10 2 7\n" + "\n".join(str((i + 1) * 11) for i in range(10)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
