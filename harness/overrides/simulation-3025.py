from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    r, c = map(int, lines[0].split())
    board = [list(line) for line in lines[1 : 1 + r]]
    n = int(lines[1 + r])
    for line in lines[2 + r : 2 + r + n]:
        col = int(line) - 1
        row = 0
        while True:
            if row + 1 == r:
                board[row][col] = "O"
                break
            if board[row + 1][col] == ".":
                row += 1
            elif board[row + 1][col] in "XO":
                if col > 0 and board[row][col - 1] == "." and board[row + 1][col - 1] == ".":
                    row += 1
                    col -= 1
                elif col + 1 < c and board[row][col + 1] == "." and board[row + 1][col + 1] == ".":
                    row += 1
                    col += 1
                else:
                    board[row][col] = "O"
                    break
    return "\n".join("".join(row) for row in board)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "5 4\n....\n....\nX...\n....\n....\n4\n1\n1\n1\n1\n",
        "7 6\n......\n......\n...XX.\n......\n......\n.XX...\n......\n6\n1\n4\n4\n6\n4\n4\n",
        "4 4\n....\n.XX.\n....\n....\n5\n2\n2\n3\n3\n1\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    hard = "8 8\n........\n...X....\n........\n..XX....\n........\n....XX..\n........\n........\n16\n" + "\n".join(str((i % 8) + 1) for i in range(16)) + "\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
