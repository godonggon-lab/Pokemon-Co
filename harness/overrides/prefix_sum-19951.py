from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    heights = list(map(int, lines[1].split()))
    diff = [0] * (n + 1)
    for line in lines[2 : 2 + m]:
        a, b, k = map(int, line.split())
        diff[a - 1] += k
        diff[b] -= k
    acc = 0
    for i in range(n):
        acc += diff[i]
        heights[i] += acc
    return " ".join(map(str, heights))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "5 3\n1 2 3 4 5\n1 3 2\n2 5 -1\n4 4 10\n",
        "1 1\n0\n1 1 5\n",
        "4 2\n10 10 10 10\n1 4 -3\n2 3 7\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    n = 100
    heights = " ".join(str(i) for i in range(n))
    ops = "\n".join(f"{i + 1} {n} {i % 7 - 3}" for i in range(50))
    stdin = f"{n} 50\n{heights}\n{ops}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
