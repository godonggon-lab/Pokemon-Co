from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress

OPS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6],
]


def solve_one(chars: list[str]) -> int:
    start = sum((1 << i) for i, ch in enumerate(chars) if ch == "H")
    q = deque([(start, 0)])
    seen = {start}
    while q:
        cur, dist = q.popleft()
        if cur in {0, 511}:
            return dist
        for op in OPS:
            nxt = cur
            for idx in op:
                nxt ^= 1 << idx
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, dist + 1))
    return -1


def expected(stdin: str) -> str:
    tokens = stdin.split()
    t = int(tokens[0])
    idx = 1
    out = []
    for _ in range(t):
        out.append(str(solve_one(tokens[idx:idx + 9])))
        idx += 9
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "1\nH H H\nH H H\nH H H\n",
        "1\nT T T\nT T T\nT T T\n",
        "1\nH T H\nT H T\nH T H\n",
        "2\nH T T\nT T T\nT T T\nH H T\nT T T\nT T T\n",
        "1\nH T H\nH T H\nT H T\n",
        "3\nH T T\nT H T\nT T H\nT H T\nH T H\nT H T\nH H H\nT T T\nH H H\n",
    ]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
