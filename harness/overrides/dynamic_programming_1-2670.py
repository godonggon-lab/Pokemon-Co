from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n = int(lines[0])
    values = [float(x) for x in lines[1 : n + 1]]
    best = cur = values[0]
    for x in values[1:]:
        cur = max(x, cur * x)
        best = max(best, cur)
    return f"{best:.3f}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n1.000\n"), edge("3\n0.500\n0.500\n2.000\n"), edge("8\n1.1\n0.7\n1.3\n0.9\n1.4\n0.8\n1.2\n0.6\n"), stress("20\n" + "\n".join(f"{1 + (i%7)/10:.1f}" for i in range(20)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
