from __future__ import annotations

from itertools import combinations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    homes = []
    chickens = []
    for r, line in enumerate(lines[1:1 + n]):
        for c, value in enumerate(map(int, line.split())):
            if value == 1:
                homes.append((r, c))
            elif value == 2:
                chickens.append((r, c))
    answer = min(
        sum(min(abs(hr - cr) + abs(hc - cc) for cr, cc in selected) for hr, hc in homes)
        for selected in combinations(chickens, m)
    )
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 1\n1 2\n0 0\n"),
        edge("5 3\n0 0 1 0 0\n0 0 2 0 1\n0 1 2 0 0\n0 0 1 0 0\n0 0 0 0 2\n"),
        stress("6 2\n1 0 2 0 1 0\n0 0 0 0 0 0\n2 0 1 0 2 0\n0 0 0 1 0 0\n1 0 2 0 0 1\n0 0 0 0 2 0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
