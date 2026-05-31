from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    board = [list(map(int, list(line))) for line in stdin.strip().splitlines()]
    used = [[False] * 8 for _ in range(7)]
    seen = [[False] * 8 for _ in range(7)]
    answer = 0

    def dfs(pos: int) -> None:
        nonlocal answer
        if pos == 56:
            answer += 1
            return
        r, c = divmod(pos, 8)
        if seen[r][c]:
            dfs(pos + 1)
            return
        seen[r][c] = True
        for dr, dc in ((1, 0), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < 7 and 0 <= nc < 8 and not seen[nr][nc]:
                a, b = sorted((board[r][c], board[nr][nc]))
                if not used[a][b]:
                    used[a][b] = True
                    seen[nr][nc] = True
                    dfs(pos + 1)
                    seen[nr][nc] = False
                    used[a][b] = False
        seen[r][c] = False

    dfs(0)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("00000000\n11111111\n22222222\n33333333\n44444444\n55555555\n66666666\n"),
        edge("00112233\n44556600\n11223344\n55660011\n22334455\n66001122\n33445566\n"),
        stress("01234567\n12345670\n23456701\n34567012\n45670123\n56701234\n67012345\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
