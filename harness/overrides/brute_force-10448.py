from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

TRIANGLES = [i * (i + 1) // 2 for i in range(1, 46)]
EUREKA = {a + b + c for a in TRIANGLES for b in TRIANGLES for c in TRIANGLES if a + b + c <= 1000}

def _solve(data: str) -> str:
    lines = data.splitlines()
    return "\n".join("1" if int(line) in EUREKA else "0" for line in lines[1:1 + int(lines[0])])

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("3\n10\n20\n1000\n"), edge("5\n1\n2\n3\n4\n5\n"), stress("10\n" + "\n".join(str(i * 97 % 1000 + 1) for i in range(10)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
