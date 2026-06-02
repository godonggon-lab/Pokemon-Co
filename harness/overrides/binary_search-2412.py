from __future__ import annotations
from collections import defaultdict, deque
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, target = map(int, lines[0].split())
    by_y = defaultdict(list)
    for line in lines[1:1 + n]:
        x, y = map(int, line.split())
        by_y[y].append(x)
    seen = {(0, 0)}
    queue = deque([(0, 0, 0)])
    while queue:
        x, y, distance = queue.popleft()
        if y == target:
            return str(distance)
        for ny in range(y - 2, y + 3):
            for nx in by_y.get(ny, []):
                if abs(nx - x) <= 2 and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append((nx, ny, distance + 1))
    return "-1"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 2\n0 2\n"), edge("2 5\n0 2\n0 5\n"), stress("6 6\n1 1\n2 2\n3 3\n3 5\n2 6\n10 6\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
