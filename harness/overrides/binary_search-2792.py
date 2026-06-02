from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    students, _ = map(int, lines[0].split())
    jewels = list(map(int, lines[1:]))
    low, high = 1, max(jewels)
    while low < high:
        mid = (low + high) // 2
        needed = sum((jewel + mid - 1) // mid for jewel in jewels)
        if needed <= students:
            high = mid
        else:
            low = mid + 1
    return str(low)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1\n7\n"), edge("7 5\n7\n1\n7\n4\n4\n"), edge("10 3\n100\n1\n1\n"), stress("100 20\n" + "\n".join(str((i * 37) % 1000 + 1) for i in range(20)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
