from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    nums = list(map(int, stdin.split()))
    money, prices = nums[0], nums[1:]

    def bnp(cash: int) -> int:
        shares = 0
        for price in prices:
            shares += cash // price
            cash %= price
        return cash + shares * prices[-1]

    def timing(cash: int) -> int:
        shares = up = down = 0
        for i in range(1, 14):
            if prices[i - 1] > prices[i]:
                down += 1
                up = 0
            elif prices[i - 1] < prices[i]:
                up += 1
                down = 0
            else:
                up = down = 0
            if down >= 3:
                shares += cash // prices[i]
                cash %= prices[i]
            if up >= 3:
                cash += shares * prices[i]
                shares = 0
        return cash + shares * prices[-1]

    a, b = bnp(money), timing(money)
    return ("BNP" if a > b else "TIMING" if a < b else "SAMESAME") + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "100\n10 10 10 10 10 10 10 10 10 10 10 10 10 10\n",
        "100\n1 2 3 4 5 6 7 8 9 10 11 12 13 14\n",
        "100\n14 13 12 11 10 9 8 7 6 5 4 3 2 1\n",
        "1000\n100 90 80 70 60 70 80 90 100 110 120 130 140 150\n",
        "500\n10 20 10 20 10 20 10 20 10 20 10 20 10 20\n",
        "1000\n50 40 30 20 10 20 30 40 50 40 30 20 10 5\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
