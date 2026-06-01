from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, health, umbrella_durability = map(int, lines[0].split())
    umbrellas = []
    start = end = (-1, -1)
    for i, line in enumerate(lines[1:1 + n]):
        for j, value in enumerate(line):
            if value == "S":
                start = (i, j)
            elif value == "E":
                end = (i, j)
            elif value == "U":
                umbrellas.append((i, j))
    visited = [False] * len(umbrellas)
    best = 10**9

    def dfs(y: int, x: int, hp: int, durability: int, distance: int) -> None:
        nonlocal best
        if distance >= best:
            return
        end_dist = abs(end[0] - y) + abs(end[1] - x)
        if end_dist <= hp + durability:
            best = min(best, distance + end_dist)
            return
        for index, (uy, ux) in enumerate(umbrellas):
            if visited[index]:
                continue
            move = abs(uy - y) + abs(ux - x)
            if move - 1 >= hp + durability:
                continue
            visited[index] = True
            next_hp = hp if move <= durability else hp + durability - move
            dfs(uy, ux, next_hp, umbrella_durability, distance + move)
            visited[index] = False

    dfs(start[0], start[1], health, 0, 0)
    return str(best if best < 10**9 else -1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2 1 1\nSE\n..\n"),
        edge("3 1 1\nS..\n...\n..E\n"),
        edge("3 2 1\nS.U\n...\n..E\n"),
        edge("4 2 2\nS...\n.U..\n..U.\n...E\n"),
        edge("5 3 1\nS....\nUUUU.\n.....\n.UUUU\n....E\n"),
        edge("5 1 3\nS....\n.....\n..U..\n.....\n....E\n"),
        stress("7 3 2\nS..U...\n.......\n..U....\n.......\n....U..\n.......\n......E\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
