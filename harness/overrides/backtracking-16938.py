from __future__ import annotations
from itertools import combinations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, low, high, diff = map(int, lines[0].split())
    scores = list(map(int, lines[1].split()))
    answer = 0
    for count in range(2, n + 1):
        for chosen in combinations(scores, count):
            total = sum(chosen)
            if low <= total <= high and max(chosen) - min(chosen) >= diff:
                answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("3 5 10 3\n1 5 6\n"), edge("4 10 20 5\n3 7 12 18\n"), stress("6 15 40 10\n1 5 10 20 25 30\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
