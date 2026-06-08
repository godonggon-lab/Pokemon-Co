from __future__ import annotations

import bisect
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    n, m = map(int, lines[0].split())
    values = sorted(int(line) for line in lines[1:1 + n])
    out = []
    for line in lines[1 + n:1 + n + m]:
        query = int(line)
        index = bisect.bisect_left(values, query)
        out.append(str(index if index < n and values[index] == query else -1))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("5 3\n1\n2\n2\n3\n5\n2\n4\n1\n"),
        edge("1 2\n7\n7\n8\n"),
        edge("3 3\n1\n1\n1\n1\n2\n0\n"),
        edge("4 4\n10\n-1\n10\n5\n-1\n5\n10\n0\n"),
        edge("6 5\n3\n3\n3\n4\n4\n5\n3\n4\n5\n2\n6\n"),
        stress("8 5\n5\n1\n3\n3\n9\n5\n1\n7\n1\n3\n5\n6\n9\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
