from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    board = [list(map(int, line.strip())) for line in data.splitlines()]
    zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9
    for i in range(9):
        for j in range(9):
            value = board[i][j]
            if value:
                bit = 1 << value
                rows[i] |= bit
                cols[j] |= bit
                boxes[i // 3 * 3 + j // 3] |= bit

    def dfs(index: int) -> bool:
        if index == len(zeros):
            return True
        best = index
        best_count = 10
        for candidate in range(index, len(zeros)):
            i, j = zeros[candidate]
            mask = (~(rows[i] | cols[j] | boxes[i // 3 * 3 + j // 3])) & 0b1111111110
            count = mask.bit_count()
            if count < best_count:
                best = candidate
                best_count = count
        zeros[index], zeros[best] = zeros[best], zeros[index]
        i, j = zeros[index]
        box = i // 3 * 3 + j // 3
        mask = (~(rows[i] | cols[j] | boxes[box])) & 0b1111111110
        for value in range(1, 10):
            bit = 1 << value
            if mask & bit:
                board[i][j] = value
                rows[i] |= bit
                cols[j] |= bit
                boxes[box] |= bit
                if dfs(index + 1):
                    return True
                rows[i] ^= bit
                cols[j] ^= bit
                boxes[box] ^= bit
                board[i][j] = 0
        zeros[index], zeros[best] = zeros[best], zeros[index]
        return False

    dfs(0)
    return "\n".join("".join(map(str, row)) for row in board)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("534678912\n672195348\n198342567\n859761423\n426853791\n713924856\n961537284\n287419635\n345286179\n"),
        edge("034678912\n672195348\n198342567\n859761423\n426853791\n713924856\n961537284\n287419635\n345286179\n"),
        edge("534678912\n672195348\n198342567\n859761423\n426853791\n713924856\n961537284\n287419635\n345286170\n"),
        edge("534678912\n672195348\n198342567\n859761423\n426853791\n713924856\n961537284\n287410635\n345286170\n"),
        edge("534678912\n672195348\n198342567\n859761423\n426853791\n713924856\n961537284\n087410635\n345286170\n"),
        stress("004678912\n672195348\n198342567\n859761423\n426853791\n713924856\n961537284\n287419635\n345286179\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
