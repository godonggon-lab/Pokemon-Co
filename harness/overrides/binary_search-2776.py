from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    index = 1
    out = []
    for _ in range(int(lines[0])):
        n = int(lines[index])
        first = set(map(int, lines[index + 1].split()))
        m = int(lines[index + 2])
        queries = list(map(int, lines[index + 3].split()))
        index += 4
        out.extend("1" if query in first else "0" for query in queries[:m])
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1\n5\n3\n5\n4\n6\n"),
        edge("1\n5\n4 1 5 2 3\n5\n1 3 7 9 5\n"),
        edge("1\n3\n-1 0 1\n5\n-1 0 1 2 -2\n"),
        edge("2\n3\n1 2 3\n3\n1 4 2\n4\n10 20 30 40\n4\n10 15 30 50\n"),
        edge("1\n5\n1 1 1 2 2\n4\n1 2 3 0\n"),
        stress("1\n10\n1 4 9 16 25 36 49 64 81 100\n6\n1 2 49 50 100 101\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
