from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _contains(board: str, target: str) -> bool:
    for start in range(len(board)):
        for step in range(1, len(board) + 1):
            end = start + step * (len(target) - 1)
            if end >= len(board):
                break
            if "".join(board[start + step * i] for i in range(len(target))) == target:
                return True
    return False


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n = int(lines[0])
    target = lines[1]
    return str(sum(_contains(board, target) for board in lines[2 : 2 + n]))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3\nABC\nABC\nAXBYC\nACB\n",
        "4\nBOJ\nBXXOXXJ\nBOJ\nBJOO\nBJO\n",
        "1\nA\nZ\n",
        "2\nCAT\nC123A123T\nCTA\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    boards = ["A" + "x" * i + "B" + "x" * i + "C" for i in range(1, 40)]
    stdin = f"{len(boards)}\nABC\n" + "\n".join(boards) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
