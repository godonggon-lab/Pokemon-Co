from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _comb(n: int, r: int) -> int:
    r = min(r, n - r)
    result = 1
    for i in range(1, r + 1):
        result = result * (n - r + i) // i
    return result


def _solve(data: str) -> str:
    lines = data.splitlines()
    t = int(lines[0])
    out = []
    for line in lines[1:1 + t]:
        n, m = map(int, line.split())
        out.append(str(_comb(m, n)))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 1\n"),
        edge("1\n1 5\n"),
        edge("1\n2 4\n"),
        edge("3\n1 1\n2 3\n3 5\n"),
        edge("4\n5 10\n10 20\n13 29\n30 30\n"),
        stress("5\n1 30\n2 30\n15 30\n20 30\n29 30\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
