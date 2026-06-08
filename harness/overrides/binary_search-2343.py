from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, disk_count = map(int, lines[0].split())
    lessons = list(map(int, lines[1].split()))
    low, high = max(lessons), sum(lessons)
    while low < high:
        mid = (low + high) // 2
        count = 1
        current = 0
        for lesson in lessons:
            if current + lesson > mid:
                count += 1
                current = 0
            current += lesson
        if count <= disk_count:
            high = mid
        else:
            low = mid + 1
    return str(low)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1\n5\n"),
        edge("3 1\n1 2 3\n"),
        edge("9 3\n1 2 3 4 5 6 7 8 9\n"),
        edge("5 5\n10 20 30 40 50\n"),
        edge("6 2\n7 7 7 7 7 7\n"),
        stress("100 10\n" + " ".join(str(i % 17 + 1) for i in range(100)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
