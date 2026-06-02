from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    grid = lines[1:1 + n]
    crosses = []
    for r in range(n):
        for c in range(m):
            size = 0
            cells = {(r, c)}
            while True:
                if all(0 <= r + dr * size < n and 0 <= c + dc * size < m and grid[r + dr * size][c + dc * size] == "#" for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    if size == 0 and grid[r][c] != "#":
                        break
                    if size > 0:
                        cells.update({(r + size, c), (r - size, c), (r, c + size), (r, c - size)})
                    crosses.append((1 + 4 * size, set(cells)))
                    size += 1
                else:
                    break
    answer = 0
    for i, (area1, cells1) in enumerate(crosses):
        for area2, cells2 in crosses[i + 1:]:
            if cells1.isdisjoint(cells2):
                answer = max(answer, area1 * area2)
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 2\n##\n"), edge("3 3\n###\n###\n###\n"), stress("5 5\n..#..\n.###.\n#####\n.###.\n..#..\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
