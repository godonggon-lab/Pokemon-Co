from __future__ import annotations
import bisect
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    index = 1
    out = []
    for _ in range(int(lines[0])):
        _, _ = map(int, lines[index].split())
        a = list(map(int, lines[index + 1].split()))
        b = sorted(map(int, lines[index + 2].split()))
        index += 3
        out.append(str(sum(bisect.bisect_left(b, value) for value in a)))
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n1 1\n2\n1\n"), edge("2\n5 3\n8 1 7 3 1\n3 6 1\n3 4\n1 1 1\n2 2 2 2\n"), stress("1\n50 50\n" + " ".join(str(i) for i in range(50)) + "\n" + " ".join(str(i*2) for i in range(50)) + "\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
