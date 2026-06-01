from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    switches = []
    count = [0] * (m + 1)
    for line in lines[1:1 + n]:
        lamps = list(map(int, line.split()))[1:]
        switches.append(lamps)
        for lamp in lamps:
            count[lamp] += 1
    return str(1 if any(all(count[lamp] >= 2 for lamp in lamps) for lamps in switches) else 0)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1\n1 1\n"), edge("2 2\n2 1 2\n1 2\n"), stress("4 5\n3 1 2 3\n2 3 4\n2 4 5\n1 5\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
