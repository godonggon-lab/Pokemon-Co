from __future__ import annotations

from collections import Counter
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, _k = map(int, lines[0].split())
    counter = Counter(map(int, lines[1].split()))
    arr = [0] * n
    for jump, count in counter.items():
        for idx in range(0, n, jump):
            arr[idx] += count
    prefix = [0]
    for value in arr:
        prefix.append(prefix[-1] + value)
    q = int(lines[2])
    out = []
    for line in lines[3 : 3 + q]:
        l, r = map(int, line.split())
        out.append(str(prefix[r + 1] - prefix[l]))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "10 4\n1 1 2 1\n3\n0 9\n2 6\n7 7\n",
        "11 3\n3 7 10\n3\n0 10\n2 6\n7 7\n",
        "6 3\n1 2 5\n2\n0 0\n1 5\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    jumps = " ".join(str((i % 11) + 1) for i in range(80))
    queries = "\n".join(["0 99", "10 50", "33 66"])
    stdin = f"100 80\n{jumps}\n3\n{queries}\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
