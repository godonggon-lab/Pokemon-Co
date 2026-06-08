from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    lines = data.splitlines()
    _, cut, target = map(int, lines[0].split())
    pieces = []
    for line in lines[1:]:
        length = int(line)
        if length >= 2 * cut:
            pieces.append(length - 2 * cut)
        elif length > cut:
            pieces.append(length - cut)
    low, high = 1, max(pieces, default=0)
    answer = -1
    while low <= high:
        mid = (low + high) // 2
        if sum(piece // mid for piece in pieces) >= target:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1 1 1\n3\n"),
        edge("1 5 1\n6\n"),
        edge("2 2 3\n10\n6\n"),
        edge("3 3 2\n3\n4\n5\n"),
        edge("4 2 10\n3\n4\n5\n6\n"),
        stress("5 3 5\n20\n12\n8\n4\n30\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
