from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    points = [tuple(map(int, line.split())) for line in lines[1:1 + n]]
    answer = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                triple = [points[i], points[j], points[k]]
                for a in range(3):
                    bx = triple[(a + 1) % 3][0] - triple[a][0]
                    by = triple[(a + 1) % 3][1] - triple[a][1]
                    cx = triple[(a + 2) % 3][0] - triple[a][0]
                    cy = triple[(a + 2) % 3][1] - triple[a][1]
                    if bx * cx + by * cy == 0:
                        answer += 1
                        break
    return str(answer)

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("3\n0 0\n1 0\n0 1\n"),
        edge("3\n0 0\n1 1\n2 2\n"),
        edge("4\n0 0\n1 0\n0 1\n1 1\n"),
        edge("5\n0 0\n2 0\n0 2\n2 2\n1 1\n"),
        edge("6\n0 0\n3 0\n0 4\n1 1\n2 2\n3 3\n"),
        stress("8\n" + "\n".join(f"{i%4} {i//4}" for i in range(8)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
