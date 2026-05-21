from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    r, c = map(int, lines[0].split())
    grid = lines[1 : 1 + r]
    words: list[str] = []
    for row in grid:
        words.extend(part for part in row.split("#") if len(part) >= 2)
    for col in range(c):
        current: list[str] = []
        for row in range(r):
            if grid[row][col] == "#":
                if len(current) >= 2:
                    words.append("".join(current))
                current = []
            else:
                current.append(grid[row][col])
        if len(current) >= 2:
            words.append("".join(current))
    return min(words)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "4 4\nluka\no#a#\nkula\ni#a#\n",
        "2 3\nabc\n#de\n",
        "3 3\na#z\nb#y\nc#x\n",
    ]
    return [edge(stdin, _solve(stdin)) for stdin in inputs]
