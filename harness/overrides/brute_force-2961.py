from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    ingredients = [tuple(map(int, line.split())) for line in lines[1:1 + n]]
    answer = 10**18
    for mask in range(1, 1 << n):
        sour = 1
        bitter = 0
        for i, (s, b) in enumerate(ingredients):
            if mask & (1 << i):
                sour *= s
                bitter += b
        answer = min(answer, abs(sour - bitter))
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n3 10\n"), edge("2\n3 8\n5 8\n"), edge("4\n1 7\n2 6\n3 8\n4 9\n"), stress("10\n" + "\n".join(f"{i%7+1} {(i*5)%13+1}" for i in range(10)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
