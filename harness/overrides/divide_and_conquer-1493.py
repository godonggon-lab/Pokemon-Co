from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    length, width, height = map(int, lines[0].split())
    n = int(lines[1])
    cubes = [0] * 20
    for line in lines[2:2 + n]:
        size, count = map(int, line.split())
        cubes[size] = count
    used = 0
    filled = 0
    for i in range(19, -1, -1):
        filled *= 8
        fit = (length >> i) * (width >> i) * (height >> i) - filled
        take = min(fit, cubes[i])
        used += take
        filled += take
    return str(used if filled == length * width * height else -1)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1 1\n1\n0 1\n"), edge("4 4 4\n1\n1 8\n"), edge("4 4 4\n1\n2 1\n"), stress("10 12 8\n4\n0 100\n1 50\n2 10\n3 1\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
