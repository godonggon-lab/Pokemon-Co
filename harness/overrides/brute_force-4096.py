from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    out = []
    for line in data.splitlines():
        if line == "0":
            break
        length = len(line)
        count = 0
        value = line
        while value != value[::-1]:
            value = str(int(value) + 1).zfill(length)
            count += 1
        out.append(str(count))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n0\n"),
        edge("9\n0\n"),
        edge("10\n0\n"),
        edge("0990\n0\n"),
        edge("1234\n9999\n0\n"),
        stress("0001\n12932\n808\n0\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
