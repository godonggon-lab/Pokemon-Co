from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, k = map(int, lines[0].split())
    dp = [0] * (k + 1)
    dp[0] = 1
    for line in lines[1 : 1 + n]:
        coin = int(line)
        for value in range(coin, k + 1):
            dp[value] += dp[value - coin]
    return str(dp[k])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3 10\n1\n2\n5\n",
        "1 5\n2\n",
        "2 0\n1\n2\n",
        "4 20\n1\n5\n10\n20\n",
        "2 3\n2\n4\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "5 100\n1\n3\n7\n11\n25\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
