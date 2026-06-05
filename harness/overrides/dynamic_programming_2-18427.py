from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n, _m, h = map(int, lines[0].split())
    students = [list(map(int, lines[i].split())) for i in range(1, n + 1)]
    dp = [1] + [0] * h
    for blocks in students:
        next_dp = dp[:]
        for height in range(h + 1):
            if dp[height] == 0:
                continue
            for block in blocks:
                if height + block <= h:
                    next_dp[height + block] = (next_dp[height + block] + dp[height]) % 10007
        dp = next_dp
    return f"{dp[h]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([
        edge("1 1 1\n1\n"),
        edge("1 3 5\n1 2 3\n"),
        edge("2 2 3\n1 2\n1 3\n"),
        edge("3 3 5\n1 2 3\n2 3 4\n1 4 5\n"),
        edge("4 4 10\n1 5\n2 4 6\n3 7\n1 2 8\n"),
        stress("5 5 12\n1 2 3\n2 5 7\n1 4 6\n3 6 9\n2 8 10\n"),
    ])
