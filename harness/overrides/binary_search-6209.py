from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    distance, rock_count, removable = map(int, lines[0].split())
    rocks = [0] + sorted(int(line) for line in lines[1:1 + rock_count]) + [distance]
    low, high = 1, distance
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        removed = 0
        last = 0
        for index in range(1, len(rocks)):
            if rocks[index] - rocks[last] < mid:
                removed += 1
            else:
                last = index
        if removed <= removable:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("10 0 0\n"), edge("25 5 2\n2\n11\n14\n17\n21\n"), stress("1000 20 5\n" + "\n".join(str((i+1)*40) for i in range(20)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
