from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, _m = map(int, lines[0].split())
    targets = list(map(int, lines[1].split()))
    queue = deque(range(1, n + 1))
    answer = 0
    for target in targets:
        index = queue.index(target)
        if index <= len(queue) // 2:
            queue.rotate(-index)
            answer += index
        else:
            move = len(queue) - index
            queue.rotate(move)
            answer += move
        queue.popleft()
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n1\n"),
        edge("5 1\n3\n"),
        edge("10 3\n1 2 3\n"),
        edge("10 3\n2 9 5\n"),
        edge("10 10\n10 9 8 7 6 5 4 3 2 1\n"),
        stress("32 6\n27 16 30 11 6 23\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
