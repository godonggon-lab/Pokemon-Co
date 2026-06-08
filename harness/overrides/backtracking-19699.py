from __future__ import annotations

from itertools import combinations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, count = map(int, lines[0].split())
    weights = list(map(int, lines[1].split()))
    limit = sum(sorted(weights, reverse=True)[:count])
    prime = [True] * (limit + 1)
    if limit >= 0:
        prime[0] = False
    if limit >= 1:
        prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if prime[i]:
            for j in range(i * i, limit + 1, i):
                prime[j] = False
    answers = sorted({sum(chosen) for chosen in combinations(weights, count) if prime[sum(chosen)]})
    return " ".join(map(str, answers if answers else [-1]))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3 2\n1 2 3\n"),
        edge("2 1\n1 1\n"),
        edge("4 3\n4 6 8 10\n"),
        edge("5 2\n1 1 1 1 1\n"),
        edge("5 3\n2 3 4 5 6\n"),
        stress("6 3\n2 5 7 11 13 17\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
