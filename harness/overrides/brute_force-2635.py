from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    n = int(data)
    best: list[int] = []
    for second in range(1, n + 1):
        seq = [n, second]
        while seq[-2] - seq[-1] >= 0:
            seq.append(seq[-2] - seq[-1])
        if len(seq) > len(best):
            best = seq
    return str(len(best)) + "\n" + " ".join(map(str, best))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n"), edge("10\n"), edge("100\n"), stress("30000\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
