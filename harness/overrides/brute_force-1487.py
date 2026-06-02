from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    buyers = [tuple(map(int, line.split())) for line in lines[1:1 + int(lines[0])]]
    best_price = 0
    best_profit = 0
    for price, _ in buyers:
        profit = sum(price - cost for want, cost in buyers if want >= price and price > cost)
        if profit > best_profit or (profit == best_profit and profit and price < best_price):
            best_profit = profit
            best_price = price
    return str(best_price if best_profit > 0 else 0)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n10 5\n"),
        edge("2\n10 11\n20 30\n"),
        edge("3\n10 1\n20 5\n30 10\n"),
        edge("4\n100 90\n80 10\n80 20\n50 1\n"),
        stress("10\n" + "\n".join(f"{(i+1)*10} {i*3}" for i in range(10)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
