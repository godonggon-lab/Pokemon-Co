from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    data = list(map(int, stdin.split()))
    n = data[0]
    wines = [0] + data[1:1 + n]
    if n == 0:
        return "0"

    dp = [0] * (n + 1)
    dp[1] = wines[1]
    if n >= 2:
        dp[2] = wines[1] + wines[2]
    for i in range(3, n + 1):
        dp[i] = max(
            dp[i - 1],
            dp[i - 2] + wines[i],
            dp[i - 3] + wines[i - 1] + wines[i],
        )
    return str(dp[n])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n10\n",
        "2\n10\n20\n",
        "3\n10\n20\n30\n",
        "4\n1\n1\n1\n1\n",
        "6\n6\n10\n13\n9\n8\n1\n",
        "7\n100\n1\n1\n100\n1\n1\n100\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]

    values = [(i * 37) % 1000 + 1 for i in range(1, 1001)]
    stdin = "1000\n" + "\n".join(map(str, values)) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
