from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    n = int(data)
    length = 3
    k = 0
    while length < n:
        k += 1
        length = length * 2 + k + 3
    while True:
        if k == 0:
            return "moo"[n - 1]
        previous = (length - k - 3) // 2
        middle = k + 3
        if n <= previous:
            length = previous
            k -= 1
        elif n <= previous + middle:
            return "m" if n == previous + 1 else "o"
        else:
            n -= previous + middle
            length = previous
            k -= 1

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("2\n"), edge("3\n"), edge("10\n"), edge("100\n"), stress("1000000000\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
