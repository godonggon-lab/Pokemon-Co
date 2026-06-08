from __future__ import annotations
from collections import defaultdict
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    groups = defaultdict(list)
    for line in lines[1:1 + n]:
        position, color = map(int, line.split())
        groups[color].append(position)
    total = 0
    for positions in groups.values():
        positions.sort()
        for i, position in enumerate(positions):
            left = position - positions[i - 1] if i else 10**18
            right = positions[i + 1] - position if i + 1 < len(positions) else 10**18
            total += min(left, right)
    return str(total)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\n1 1\n3 1\n"),
        edge("4\n1 1\n2 1\n10 2\n13 2\n"),
        edge("5\n1 1\n5 1\n3 1\n10 2\n20 2\n"),
        edge("6\n1 1\n4 1\n8 1\n2 2\n3 2\n10 2\n"),
        edge("8\n1 1\n2 1\n3 1\n4 1\n10 2\n20 2\n30 2\n40 2\n"),
        stress("30\n" + "\n".join(f"{i*3} {i%5}" for i in range(30)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
