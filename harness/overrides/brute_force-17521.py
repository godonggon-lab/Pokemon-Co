from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, cash = map(int, lines[0].split())
    prices = [int(line) for line in lines[1:1 + n]]
    stock = 0
    for i in range(n - 1):
        if prices[i] < prices[i + 1]:
            stock += cash // prices[i]
            cash %= prices[i]
        elif prices[i] > prices[i + 1]:
            cash += stock * prices[i]
            stock = 0
    return str(cash + stock * prices[-1])

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 10\n5\n"),
        edge("2 10\n5\n10\n"),
        edge("3 10\n5\n10\n3\n"),
        edge("4 100\n10\n9\n8\n7\n"),
        edge("5 10\n1\n2\n3\n4\n5\n"),
        stress("6 100\n5\n7\n4\n10\n9\n12\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
