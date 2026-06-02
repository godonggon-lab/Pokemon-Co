from __future__ import annotations
from collections import Counter
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
        counter = Counter()
        for line in lines[cursor:cursor + n]:
            _name, kind = line.split()
            counter[kind] += 1
        cursor += n
        answer = 1
        for count in counter.values():
            answer *= count + 1
        out.append(str(answer - 1))
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n0\n"), edge("1\n3\nhat headgear\nsunglasses eyewear\nturban headgear\n"), edge("2\n2\na x\nb x\n3\na x\nb y\nc z\n"), stress("1\n10\n" + "\n".join(f"item{i} kind{i%3}" for i in range(10)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
