from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    t = int(lines[0])
    out = []
    for line in lines[1:1 + t]:
        n, m = map(int, line.split())
        count = 0
        for a in range(1, n):
            for b in range(a + 1, n):
                if (a * a + b * b + m) % (a * b) == 0:
                    count += 1
        out.append(str(count))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n2 1\n"),
        edge("1\n5 1\n"),
        edge("2\n10 1\n10 2\n"),
        edge("3\n20 3\n30 4\n40 5\n"),
        edge("4\n5 1\n10 10\n50 7\n70 9\n"),
        stress("5\n100 1\n100 10\n100 50\n99 33\n75 12\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
