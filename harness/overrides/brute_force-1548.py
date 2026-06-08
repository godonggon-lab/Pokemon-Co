from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    nums = sorted(map(int, lines[1].split()))
    answer = min(n, 2)
    for i in range(n):
        for j in range(i + 2, n):
            if nums[i] + nums[i + 1] > nums[j]:
                answer = max(answer, j - i + 1)
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n5\n"), edge("2\n1 100\n"), edge("3\n1 2 3\n"), edge("3\n2 3 4\n"), edge("5\n1 1 1 2 3\n"), stress("20\n" + " ".join(str(i % 9 + 1) for i in range(20)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
