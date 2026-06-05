from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    r, c, w = map(int, data.split())
    comb = [[0] * 31 for _ in range(31)]
    for i in range(1, 31):
        comb[i][1] = comb[i][i] = 1
        for j in range(2, i):
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]
    answer = 0
    for i in range(w):
        for j in range(i + 1):
            answer += comb[r + i][c + j]
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1 1\n"), edge("3 1 4\n"), edge("5 3 5\n"), stress("10 5 10\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
