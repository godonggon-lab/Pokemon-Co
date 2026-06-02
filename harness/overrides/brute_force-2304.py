from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    pillars = sorted(tuple(map(int, line.split())) for line in lines[1:1 + n])
    max_height = max(height for _, height in pillars)
    max_positions = [x for x, height in pillars if height == max_height]
    left_peak = max_positions[0]
    right_peak = max_positions[-1]
    area = (right_peak - left_peak + 1) * max_height
    current_x, current_h = pillars[0]
    for x, height in pillars:
        if x > left_peak:
            break
        if height > current_h:
            area += (x - current_x) * current_h
            current_x, current_h = x, height
    current_x, current_h = pillars[-1]
    for x, height in reversed(pillars):
        if x < right_peak:
            break
        if height > current_h:
            area += (current_x - x) * current_h
            current_x, current_h = x, height
    return str(area)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n5 10\n"), edge("3\n1 2\n2 5\n3 2\n"), edge("4\n1 5\n2 3\n4 5\n5 1\n"), edge("7\n2 4\n11 4\n15 8\n4 6\n5 3\n8 10\n13 6\n"), stress("20\n" + "\n".join(f"{i*2+1} {(i*7)%13+1}" for i in range(20)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
