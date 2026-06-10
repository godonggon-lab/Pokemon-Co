from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n, m = nums[:2]
    idx = 2
    ps = [[0] * (m + 1)]
    for _ in range(n):
        row = nums[idx : idx + m]
        idx += m
        acc = [0]
        for x in row:
            acc.append(acc[-1] + x)
        ps.append([ps[-1][j] + acc[j] for j in range(m + 1)])
    k = nums[idx]
    idx += 1
    out = []
    for _ in range(k):
        x1, y1, x2, y2 = nums[idx : idx + 4]
        idx += 4
        out.append(str(ps[x2][y2] - ps[x1 - 1][y2] - ps[x2][y1 - 1] + ps[x1 - 1][y1 - 1]))
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n5\n1\n1 1 1 1\n"),
        edge("3 3\n1 2 3\n4 5 6\n7 8 9\n3\n1 1 3 3\n2 2 3 3\n1 2 2 3\n"),
        edge("1 4\n1 2 3 4\n3\n1 1 1 4\n1 2 1 3\n1 4 1 4\n"),
        edge("4 1\n2\n4\n6\n8\n3\n1 1 4 1\n2 1 3 1\n4 1 4 1\n"),
        edge("2 3\n10 20 30\n40 50 60\n4\n1 1 1 1\n1 3 2 3\n2 1 2 2\n1 2 2 3\n"),
        stress("10 10\n" + "\n".join(" ".join(str((r+c)%10) for c in range(10)) for r in range(10)) + "\n1\n1 1 10 10\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
