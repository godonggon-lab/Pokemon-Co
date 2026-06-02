from __future__ import annotations
import bisect
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    pairs = [tuple(map(int, line.split())) for line in lines[1:1 + int(lines[0])]]
    lows = sorted(value - delta for value, delta in pairs)
    highs = sorted(value + delta for value, delta in pairs)
    out = []
    for value, delta in pairs:
        best = len(pairs) - bisect.bisect_right(lows, value + delta) + 1
        worst = len(pairs) - bisect.bisect_left(highs, value - delta)
        out.append(f"{best} {worst}")
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3\n10 1\n20 2\n30 3\n"),
        edge("4\n100 0\n90 20\n80 10\n70 5\n"),
        stress("6\n50 10\n50 0\n40 15\n60 5\n30 20\n70 1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
