from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    s, n, k, r1, r2, c1, c2 = map(int, data.split())
    size = n ** s

    def black(r: int, c: int, current_size: int, level: int) -> bool:
        if level == 0:
            return False
        unit = current_size // n
        a, b = r // unit, c // unit
        low = (n - k) // 2
        high = low + k
        if low <= a < high and low <= b < high:
            return True
        return black(r % unit, c % unit, unit, level - 1)

    return "\n".join(
        "".join("1" if black(r, c, size, s) else "0" for c in range(c1, c2 + 1))
        for r in range(r1, r2 + 1)
    )

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 3 1 0 2 0 2\n"),
        edge("1 5 3 1 3 1 3\n"),
        edge("2 3 1 0 8 0 8\n"),
        edge("2 3 1 4 4 0 8\n"),
        edge("2 5 1 10 14 10 14\n"),
        stress("3 3 1 5 15 4 14\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
