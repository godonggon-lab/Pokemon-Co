from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    values = list(map(int, data.split()))
    n = values[0]
    charms = values[1:1 + n]
    total = sum(charms)
    dp = {(0, 0)}
    for charm in charms:
        next_dp = set(dp)
        for a, b in dp:
            next_dp.add((a + charm, b))
            next_dp.add((a, b + charm))
        dp = next_dp
    return f"{max(min(a, b, total - a - b) for a, b in dp if a + b <= total)}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("3\n1 2 3\n"), edge("4\n1 1 1 1\n"), stress("5\n2 3 5 7 11\n")])
