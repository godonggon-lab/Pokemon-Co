from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    s = lines[1]
    order = {"B": "O", "O": "J", "J": "B"}
    inf = 10**18
    dp = [inf] * n
    dp[0] = 0
    for i in range(n):
        if dp[i] == inf:
            continue
        for j in range(i + 1, n):
            if s[j] == order[s[i]]:
                dp[j] = min(dp[j], dp[i] + (j - i) ** 2)
    return "-1" if dp[-1] == inf else str(dp[-1])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "9\nBOJBOJBOJ\n",
        "3\nBOJ\n",
        "3\nBBB\n",
        "6\nBJOBOJ\n",
        "1\nB\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "BOJ" * 40
    cases.append(stress(f"{len(s)}\n{s}\n", _solve(f"{len(s)}\n{s}\n")))
    return cases
