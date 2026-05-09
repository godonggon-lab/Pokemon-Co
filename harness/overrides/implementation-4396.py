from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def expected(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    mines = lines[1:1 + n]
    opened = [list(row) for row in lines[1 + n:1 + 2 * n]]
    hit = any(opened[i][j] == "x" and mines[i][j] == "*" for i in range(n) for j in range(n))
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(n):
        for j in range(n):
            if opened[i][j] == "x" and mines[i][j] != "*":
                opened[i][j] = str(sum(0 <= i + dy < n and 0 <= j + dx < n and mines[i + dy][j + dx] == "*" for dy, dx in dirs))
            elif opened[i][j] != "x":
                opened[i][j] = "."
    if hit:
        for i in range(n):
            for j in range(n):
                if mines[i][j] == "*":
                    opened[i][j] = "*"
    return "\n".join("".join(row) for row in opened) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\n.\nx\n",
        "1\n*\nx\n",
        "3\n*..\n...\n..*\nxxx\nx.x\nxxx\n",
        "3\n*..\n...\n..*\n...\n.x.\n...\n",
        "4\n*...\n....\n..*.\n....\nxxxx\n....\n..x.\n....\n",
        "5\n*...*\n.....\n..*..\n.....\n*...*\nxxxxx\nx...x\n..x..\nx...x\nxxxxx\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
