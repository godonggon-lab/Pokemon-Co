from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    board = [list(line) for line in lines[1:1 + n]]

    def best() -> int:
        result = 1
        for i in range(n):
            row = col = 1
            for j in range(1, n):
                row = row + 1 if board[i][j] == board[i][j - 1] else 1
                col = col + 1 if board[j][i] == board[j - 1][i] else 1
                result = max(result, row, col)
        return result

    answer = best()
    for i in range(n):
        for j in range(n):
            if j + 1 < n:
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                answer = max(answer, best())
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            if i + 1 < n:
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                answer = max(answer, best())
                board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    rows = [("CPZY" * 4)[i:i + 8] for i in range(8)]
    cases = [edge("3\nCCP\nCCP\nPPC\n"), edge("4\nPPPP\nCYZY\nCCPY\nPPCC\n"), edge("5\nYCPZY\nCYZZP\nCCPPP\nYCYZC\nCPPZZ\n"), stress("8\n" + "\n".join(rows) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
