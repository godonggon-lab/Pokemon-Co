from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    games = [(i, j) for i in range(6) for j in range(i + 1, 6)]

    def possible(result: list[list[int]], index: int = 0) -> bool:
        if index == 15:
            return all(value == 0 for row in result for value in row)
        a, b = games[index]
        for ra, rb in ((0, 2), (1, 1), (2, 0)):
            if result[a][ra] and result[b][rb]:
                result[a][ra] -= 1
                result[b][rb] -= 1
                if possible(result, index + 1):
                    return True
                result[a][ra] += 1
                result[b][rb] += 1
        return False

    nums = list(map(int, data.split()))
    out = []
    for offset in range(0, len(nums), 18):
        result = [nums[offset + i * 3:offset + i * 3 + 3] for i in range(6)]
        out.append("1" if sum(map(sum, result)) == 30 and possible(result) else "0")
    return " ".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("5 0 0 0 0 5 0 5 0 0 0 5 0 0 5 0 5 0\n0 0 5 0 0 5 0 0 5 0 0 5 0 0 5 0 0 5\n1 4 0 2 2 1 2 0 3 2 0 3 1 3 1 2 1 2\n0 5 0 0 0 5 2 0 3 2 0 3 1 0 4 0 0 5\n"),
        edge("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n"),
        edge("5 0 0 4 1 0 3 1 1 2 1 2 1 1 3 0 0 5\n"),
        edge("1 1 3 1 1 3 1 1 3 1 1 3 1 1 3 1 1 3\n"),
        edge("5 0 0 5 0 0 5 0 0 5 0 0 5 0 0 5 0 0\n"),
        stress("0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n5 0 0 4 1 0 3 1 1 2 1 2 1 1 3 0 0 5\n5 0 0 5 0 0 5 0 0 5 0 0 5 0 0 5 0 0\n1 1 3 1 1 3 1 1 3 1 1 3 1 1 3 1 1 3\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
