from __future__ import annotations
from itertools import combinations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n = int(stdin)
    values = []
    for length in range(1, 11):
        for comb in combinations(range(10), length):
            values.append(int("".join(map(str, sorted(comb, reverse=True)))))
    values.sort()
    return str(values[n - 1] if 1 <= n <= len(values) else -1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("10\n"), edge("1023\n"), edge("1024\n"), stress("500\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
