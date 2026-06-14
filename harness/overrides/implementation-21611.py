from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, m = map(int, lines[0].split())
    board = [list(map(int, line.split())) for line in lines[1 : 1 + n]]
    spells = [tuple(map(int, line.split())) for line in lines[1 + n : 1 + n + m]]
    center = n // 2
    positions: list[tuple[int, int]] = []
    r = c = center
    for length in range(1, n):
        for dr, dc, count in ((0, -1, length), (1, 0, length), (0, 1, length + 1), (-1, 0, length + 1)):
            for _ in range(count):
                r += dr
                c += dc
                if 0 <= r < n and 0 <= c < n:
                    positions.append((r, c))
        if len(positions) >= n * n - 1:
            break
    positions = positions[: n * n - 1]
    dir_map = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    score = [0, 0, 0, 0]

    def flatten() -> list[int]:
        return [board[row][col] for row, col in positions if board[row][col] != 0]

    def write(values: list[int]) -> None:
        for idx, (row, col) in enumerate(positions):
            board[row][col] = values[idx] if idx < len(values) else 0

    for d, s in spells:
        dr, dc = dir_map[d]
        for step in range(1, s + 1):
            rr, cc = center + dr * step, center + dc * step
            if 0 <= rr < n and 0 <= cc < n:
                board[rr][cc] = 0
        values = flatten()
        changed = True
        while changed:
            changed = False
            nxt: list[int] = []
            i = 0
            while i < len(values):
                j = i
                while j < len(values) and values[j] == values[i]:
                    j += 1
                if j - i >= 4:
                    score[values[i]] += j - i
                    changed = True
                else:
                    nxt.extend(values[i:j])
                i = j
            values = nxt
        transformed: list[int] = []
        i = 0
        while i < len(values) and len(transformed) < len(positions):
            j = i
            while j < len(values) and values[j] == values[i]:
                j += 1
            transformed.extend([j - i, values[i]])
            i = j
        write(transformed[: len(positions)])
    return str(score[1] + score[2] * 2 + score[3] * 3)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "3 1\n0 0 0\n0 0 0\n0 0 0\n1 1\n",
        "5 1\n1 1 1 1 1\n1 1 1 1 1\n1 1 0 1 1\n1 1 1 1 1\n1 1 1 1 1\n1 1\n",
        "5 2\n1 2 3 2 1\n2 2 2 2 2\n3 3 0 3 3\n1 1 1 1 1\n2 3 2 3 2\n1 2\n3 1\n",
        "3 2\n1 1 1\n1 0 1\n1 1 1\n1 1\n2 1\n",
        "5 1\n0 0 0 0 0\n0 2 2 2 0\n0 2 0 2 0\n0 2 2 2 0\n0 0 0 0 0\n4 2\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    board = "\n".join(" ".join(str((i + j) % 3 + 1) if (i, j) != (3, 3) else "0" for j in range(7)) for i in range(7))
    spells = "\n".join(["1 3", "2 2", "3 3", "4 2", "1 1"])
    hard = f"7 5\n{board}\n{spells}\n"
    cases.append(stress(hard, _solve(hard)))
    return cases
