from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    n, k = map(int, data.split())
    queue = deque(range(1, n + 1))
    out = []
    while queue:
        queue.rotate(-(k - 1))
        out.append(str(queue.popleft()))
    return "<" + ", ".join(out) + ">"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n"),
        edge("3 1\n"),
        edge("3 2\n"),
        edge("7 3\n"),
        edge("5 7\n"),
        stress("10 4\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
