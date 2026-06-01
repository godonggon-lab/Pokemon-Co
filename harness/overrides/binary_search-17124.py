from __future__ import annotations
import bisect
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    out = []
    index = 1
    for _ in range(int(lines[0])):
        n, m = map(int, lines[index].split())
        a = list(map(int, lines[index + 1].split()))
        b = sorted(map(int, lines[index + 2].split()))
        index += 3
        total = 0
        for value in a:
            pos = bisect.bisect_left(b, value)
            candidates = []
            if pos < m:
                candidates.append(b[pos])
            if pos:
                candidates.append(b[pos - 1])
            total += min(candidates, key=lambda item: (abs(item - value), item))
        out.append(str(total))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1\n1 1\n5\n7\n"), edge("1\n3 3\n1 5 10\n2 6 11\n"), stress("2\n4 5\n1 4 8 20\n2 3 9 15 30\n2 2\n100 1\n50 150\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
