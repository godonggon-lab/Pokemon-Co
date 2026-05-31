from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.strip().splitlines()
    n, target = map(int, lines[0].split())
    values = list(map(int, lines[1].split()))
    answer = 0
    for mask in range(1, 1 << n):
        total = sum(values[i] for i in range(n) if mask & (1 << i))
        if total == target:
            answer += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n1\n"),
        edge("1 0\n1\n"),
        edge("3 0\n-1 0 1\n"),
        edge("5 0\n-7 -3 -2 5 8\n"),
        edge("6 3\n1 2 3 4 -1 -2\n"),
        stress("10 5\n1 1 1 1 1 2 2 2 -1 -2\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
