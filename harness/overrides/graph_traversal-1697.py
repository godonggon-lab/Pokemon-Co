from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


MAX_POS = 100000


def _solve(stdin: str) -> str:
    start, target = map(int, stdin.split())
    if start >= target:
        return str(start - target)

    dist = [-1] * (MAX_POS + 1)
    q: deque[int] = deque([start])
    dist[start] = 0
    while q:
        cur = q.popleft()
        if cur == target:
            return str(dist[cur])
        for nxt in (cur - 1, cur + 1, cur * 2):
            if 0 <= nxt <= MAX_POS and dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    raise RuntimeError("unreachable")


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "0 0\n",
        "10 1\n",
        "5 17\n",
        "1 2\n",
        "0 100000\n",
        "99999 100000\n",
        "100000 0\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("12345 98765\n", _solve("12345 98765\n")))
    return cases
