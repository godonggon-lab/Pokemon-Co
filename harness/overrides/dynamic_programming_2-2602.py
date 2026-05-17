from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    target, devil, angel = stdin.split()
    bridges = [devil, angel]
    n = len(target)
    m = len(devil)
    dp = [[[0] * m for _ in range(n)] for _ in range(2)]

    for b in range(2):
        for pos, ch in enumerate(bridges[b]):
            if ch == target[0]:
                dp[b][0][pos] = 1

    for idx in range(1, n):
        for b in range(2):
            other = 1 - b
            running = 0
            for pos in range(m):
                if pos > 0:
                    running += dp[other][idx - 1][pos - 1]
                if bridges[b][pos] == target[idx]:
                    dp[b][idx][pos] = running

    return str(sum(dp[0][n - 1]) + sum(dp[1][n - 1]))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "R\nR\nR\n",
        "RING\nRINGS\nGRING\n",
        "GG\nGGGG\nGGGG\n",
        "RS\nSR\nRS\n",
        "RINGS\nRRRRRIIIIINNNNNGGGGGSSSSS\nSSSSSGGGGGNNNNNIIIIIRRRRR\n",
        "RING\nRRRR\nIIII\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]

    target = "RINGS" * 4
    devil = "RINGS" * 20
    angel = "SGNIR" * 20
    stdin = f"{target}\n{devil}\n{angel}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
