from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    out = []
    for line in lines[1:1 + int(lines[0])]:
        start, end = map(int, line.split())
        out.append(str(sum(str(value).count("0") for value in range(start, end + 1))))
    return "\n".join(out)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n0 0\n"),
        edge("1\n1 9\n"),
        edge("2\n10 10\n99 101\n"),
        edge("3\n0 10\n10 20\n100 200\n"),
        edge("2\n1000 1000\n1001 1010\n"),
        stress("2\n1 1000\n500 5000\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
