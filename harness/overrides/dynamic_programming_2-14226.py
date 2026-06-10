from __future__ import annotations
from collections import deque
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    target = int(data.strip())
    limit = 1001
    dist = [[-1] * limit for _ in range(limit)]
    dist[1][0] = 0
    q = deque([(1, 0)])
    while q:
        screen, clip = q.popleft()
        if screen == target:
            return f"{dist[screen][clip]}\n"
        for ns, nc in ((screen, screen), (screen + clip, clip), (screen - 1, clip)):
            if 0 <= ns < limit and 0 <= nc < limit and dist[ns][nc] == -1:
                dist[ns][nc] = dist[screen][clip] + 1
                q.append((ns, nc))
    raise AssertionError("unreachable target")


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n"),
        edge("2\n"),
        edge("3\n"),
        edge("6\n"),
        edge("11\n"),
        stress("18\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
