from __future__ import annotations

from collections import defaultdict
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, k = map(int, lines[0].split())
    arr = list(map(int, lines[1].split()))
    counter = defaultdict(int)
    counter[0] = 1
    prefix = 0
    answer = 0
    for idx, value in enumerate(arr, 1):
        prefix += value
        key = prefix - idx * k
        answer += counter[key]
        counter[key] += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "6 1\n1 1 1 1 1 1\n",
        "5 3\n1 2 3 4 5\n",
        "4 0\n1 -1 2 -2\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "100 7\n" + " ".join(["7"] * 100) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
