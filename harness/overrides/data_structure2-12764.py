from __future__ import annotations
import heapq
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    people = sorted(tuple(map(int, line.split())) for line in lines[1:1 + n])
    using: list[tuple[int, int]] = []
    free: list[int] = []
    counts: list[int] = []
    for start, end in people:
        while using and using[0][0] <= start:
            _end, seat = heapq.heappop(using)
            heapq.heappush(free, seat)
        if free:
            seat = heapq.heappop(free)
        else:
            seat = len(counts)
            counts.append(0)
        counts[seat] += 1
        heapq.heappush(using, (end, seat))
    return str(len(counts)) + "\n" + " ".join(map(str, counts))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 2\n"),
        edge("3\n1 2\n2 3\n3 4\n"),
        edge("3\n1 5\n2 3\n4 6\n"),
        edge("4\n1 10\n2 9\n3 8\n4 7\n"),
        edge("5\n1 2\n1 3\n1 4\n2 5\n3 6\n"),
        stress("20\n" + "\n".join(f"{i} {i+10}" for i in range(20)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
