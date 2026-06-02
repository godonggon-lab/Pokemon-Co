from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    nums = list(map(int, lines[1].split()))
    seen = {0}
    for value in nums:
        seen |= {current + value for current in list(seen)}
    answer = 1
    while answer in seen:
        answer += 1
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n1\n"), edge("3\n1 1 2\n"), edge("5\n5 1 2 7 3\n"), stress("20\n" + " ".join(str(i % 10 + 1) for i in range(20)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
