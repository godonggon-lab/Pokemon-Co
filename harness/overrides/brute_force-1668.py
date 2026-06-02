from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _visible(heights: list[int]) -> int:
    count = highest = 0
    for height in heights:
        if height > highest:
            count += 1
            highest = height
    return count


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    heights = [int(line) for line in lines[1:1 + n]]
    return f"{_visible(heights)}\n{_visible(heights[::-1])}"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n10\n"),
        edge("5\n1\n2\n3\n4\n5\n"),
        edge("5\n5\n4\n3\n2\n1\n"),
        edge("5\n1\n3\n2\n5\n4\n"),
        stress("20\n" + "\n".join(str((i * 7) % 11 + 1) for i in range(20)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
