from __future__ import annotations
from functools import lru_cache
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    counts = tuple(nums[1 : 1 + n])

    @lru_cache(None)
    def dp(state: tuple[int, ...], last1: int, last2: int) -> int:
        if sum(state) == 0:
            return 1
        res = 0
        st = list(state)
        for i in range(n):
            if st[i] and i != last1 and i != last2:
                st[i] -= 1
                res += dp(tuple(st), i, last1)
                st[i] += 1
        return res

    return f"{dp(counts, -1, -1)}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3\n1\n1\n1\n"),
        edge("3\n2\n1\n1\n"),
        stress("4\n2\n2\n1\n1\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
