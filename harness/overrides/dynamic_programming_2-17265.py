from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.strip().splitlines()
    n = int(lines[0])
    grid = [line.split() for line in lines[1:]]
    max_dp = [[-10**18] * n for _ in range(n)]
    min_dp = [[10**18] * n for _ in range(n)]
    max_dp[0][0] = min_dp[0][0] = int(grid[0][0])

    def calc(left: int, op: str, right: str) -> int:
        value = int(right)
        if op == "+":
            return left + value
        if op == "-":
            return left - value
        return left * value

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 1:
                continue
            for pi, pj, oi, oj in ((i - 2, j, i - 1, j), (i, j - 2, i, j - 1), (i - 1, j - 1, i - 1, j), (i - 1, j - 1, i, j - 1)):
                if 0 <= pi < n and 0 <= pj < n and 0 <= oi < n and 0 <= oj < n:
                    for prev in (max_dp[pi][pj], min_dp[pi][pj]):
                        if -10**17 < prev < 10**17:
                            result = calc(prev, grid[oi][oj], grid[i][j])
                            max_dp[i][j] = max(max_dp[i][j], result)
                            min_dp[i][j] = min(min_dp[i][j], result)
    return f"{max_dp[-1][-1]} {min_dp[-1][-1]}\n"


def _with_expected(cases: List[GeneratedCase]) -> List[GeneratedCase]:
    return [{**case, "expected": _solve(case["input"])} for case in cases]


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return _with_expected([edge("1\n7\n"), edge("3\n1 + 2\n* 3 -\n4 + 5\n"), stress("5\n1 + 2 * 3\n- 4 + 5 -\n6 * 7 + 8\n+ 9 - 1 *\n2 + 3 - 4\n")])
