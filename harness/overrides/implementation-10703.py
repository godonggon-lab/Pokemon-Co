from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    r, s = map(int, lines[0].split())
    grid = [list(row) for row in lines[1 : 1 + r]]
    drop = r
    for c in range(s):
        meteor = -1
        ground = r
        for i in range(r):
            if grid[i][c] == "X":
                meteor = i
            elif grid[i][c] == "#" and meteor != -1:
                ground = i
                break
        if meteor != -1:
            drop = min(drop, ground - meteor - 1)
    result = [["." for _ in range(s)] for _ in range(r)]
    for i in range(r):
        for j in range(s):
            if grid[i][j] == "#":
                result[i][j] = "#"
            elif grid[i][j] == "X":
                result[i + drop][j] = "X"
    return "\n".join("".join(row) for row in result)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "5 5\n..X..\n.XXX.\n.....\n.....\n#####\n",
        "4 3\nX..\n...\n...\n###\n",
        "6 6\n.XX...\n..X...\n......\n...#..\n...#..\n######\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "8 8\n" + "\n".join(["XX......", ".X......", "........", "........", "........", "........", "........", "########"]) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
