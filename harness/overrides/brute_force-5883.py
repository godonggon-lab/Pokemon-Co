from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    nums = [int(line) for line in lines[1:1 + n]]
    answer = 0
    for removed in set(nums):
        previous = None
        current = best = 0
        for value in nums:
            if value == removed:
                continue
            if value == previous:
                current += 1
            else:
                previous = value
                current = 1
            best = max(best, current)
        answer = max(answer, best)
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n5\n"),
        edge("3\n1\n1\n1\n"),
        edge("5\n1\n2\n1\n1\n2\n"),
        edge("6\n1\n2\n1\n2\n1\n2\n"),
        edge("7\n1\n2\n2\n1\n2\n2\n1\n"),
        stress("30\n" + "\n".join(str((i // 3) % 4) for i in range(30)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
