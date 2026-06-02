from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    t = int(lines[0])
    cursor = 1
    out = []
    for _ in range(t):
        n = int(lines[cursor])
        cursor += 1
        nums = list(map(int, lines[cursor].split()))
        cursor += 1
        best = current = nums[0]
        for value in nums[1:n]:
            current = max(value, current + value)
            best = max(best, current)
        out.append(str(best))
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n1\n-5\n"), edge("2\n5\n1 2 3 4 5\n5\n-1 -2 -3 -4 -5\n"), stress("1\n50\n" + " ".join(str((i * 7) % 21 - 10) for i in range(50)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
