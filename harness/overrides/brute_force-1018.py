from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    board = lines[1:1 + n]
    answer = 64
    for row in range(n - 7):
        for col in range(m - 7):
            for first in "WB":
                count = 0
                for i in range(8):
                    for j in range(8):
                        expected = first if (i + j) % 2 == 0 else ("B" if first == "W" else "W")
                        count += board[row + i][col + j] != expected
                answer = min(answer, count)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("8 8\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\n"),
        edge("8 8\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\nBBBBBBBB\n"),
        edge("10 13\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nWWWWWWWWWWBWB\nWWWWWWWWWWBWB\n"),
        stress("9 9\n" + "\n".join("WBWBWBWBW" if i % 2 == 0 else "BWBWBWBWB" for i in range(9)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
