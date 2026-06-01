from __future__ import annotations
from collections import deque
from itertools import combinations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    board = data.splitlines()
    positions = range(25)
    answer = 0
    for selected in combinations(positions, 7):
        if sum(board[pos // 5][pos % 5] == "S" for pos in selected) < 4:
            continue
        selected_set = set(selected)
        queue = deque([selected[0]])
        seen = {selected[0]}
        while queue:
            pos = queue.popleft()
            x, y = divmod(pos, 5)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                next_pos = nx * 5 + ny
                if 0 <= nx < 5 and 0 <= ny < 5 and next_pos in selected_set and next_pos not in seen:
                    seen.add(next_pos)
                    queue.append(next_pos)
        if len(seen) == 7:
            answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("SSSSS\nSSSSS\nSSSSS\nSSSSS\nSSSSS\n"),
        edge("YYYYY\nYYYYY\nYYYYY\nYYYYY\nYYYYY\n"),
        stress("SYSYS\nYSYSY\nSYSYS\nYSYSY\nSYSYS\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
