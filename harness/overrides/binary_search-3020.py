from __future__ import annotations
import bisect
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, height = map(int, lines[0].split())
    bottom, top = [], []
    for index, line in enumerate(lines[1:1 + n]):
        value = int(line)
        if index % 2 == 0:
            bottom.append(value)
        else:
            top.append(value)
    bottom.sort()
    top.sort()
    best = n + 1
    count = 0
    for current in range(1, height + 1):
        hit = len(bottom) - bisect.bisect_left(bottom, current)
        hit += len(top) - bisect.bisect_left(top, height - current + 1)
        if hit < best:
            best, count = hit, 1
        elif hit == best:
            count += 1
    return f"{best} {count}"

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("2 1\n1\n1\n"), edge("6 7\n1\n5\n3\n3\n5\n1\n"), stress("20 10\n" + "\n".join(str(i%10+1) for i in range(20)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
