from __future__ import annotations
import bisect
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    powers = list(map(int, lines[1].split()))
    limits = list(map(int, lines[2].split()))
    return " ".join(str(bisect.bisect_right(limits, power) - index - 1) for index, power in enumerate(powers))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n5\n5\n"), edge("5\n3 5 7 9 10\n1 4 6 8 10\n"), stress("6\n2 4 8 16 32 64\n1 2 4 8 16 32\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
