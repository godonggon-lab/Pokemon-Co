from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, start, limit = map(int, lines[0].split())
    volumes = list(map(int, lines[1].split()))
    current = {start}
    for diff in volumes[:n]:
        nxt = set()
        for volume in current:
            if volume + diff <= limit:
                nxt.add(volume + diff)
            if volume - diff >= 0:
                nxt.add(volume - diff)
        current = nxt
        if not current:
            break
    return str(max(current) if current else -1)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 5 10\n5\n"), edge("2 5 10\n6 6\n"), stress("5 10 20\n5 3 7 10 2\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
