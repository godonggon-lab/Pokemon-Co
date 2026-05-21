from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    first, second = stdin.strip().splitlines()
    n = len(first)
    a = deque(sorted(first)[: (n + 1) // 2])
    b = deque(sorted(second, reverse=True)[: n // 2])
    answer = [""] * n
    left = 0
    right = n - 1
    for turn in range(n):
        if turn % 2 == 0:
            if b and a[0] >= b[0]:
                answer[right] = a.pop()
                right -= 1
            else:
                answer[left] = a.popleft()
                left += 1
        else:
            if a and b[0] <= a[0]:
                answer[right] = b.pop()
                right -= 1
            else:
                answer[left] = b.popleft()
                left += 1
    return "".join(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "ioi\nimo\n",
        "koooosaga\ncubelover\n",
        "cubehater\ncubelover\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "abcdefghijklmnopqrstuvwxyz\nzyxwvutsrqponmlkjihgfedcba\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
