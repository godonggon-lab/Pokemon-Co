from __future__ import annotations
from itertools import combinations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    for selected in combinations(nums, 7):
        if sum(selected) == 100:
            return "\n".join(map(str, selected))
    return ""

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("7\n8\n10\n13\n15\n19\n20\n23\n25\n"),
        edge("20\n7\n23\n19\n10\n15\n25\n8\n13\n"),
        edge("1\n2\n3\n4\n5\n6\n7\n72\n80\n"),
        edge("10\n10\n10\n10\n10\n10\n10\n15\n25\n"),
        edge("5\n6\n7\n8\n9\n10\n20\n35\n40\n"),
        stress("1\n2\n3\n4\n5\n6\n7\n72\n99\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
