from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    m = nums[1]
    vip = nums[2 : 2 + m]
    fib = [1] * (n + 2)
    for i in range(2, n + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    ans = 1
    prev = 0
    for seat in vip + [n + 1]:
        ans *= fib[seat - prev - 1]
        prev = seat
    return f"{ans}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n0\n"), edge("2\n1\n1\n"), edge("5\n0\n"), edge("9\n2\n4\n7\n"), edge("10\n3\n1\n5\n10\n"), stress("40\n4\n5\n10\n20\n35\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
