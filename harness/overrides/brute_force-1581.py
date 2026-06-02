from __future__ import annotations
from functools import lru_cache
from typing import List
from harness.cases import GeneratedCase, edge, stress

def _solve(data: str) -> str:
    counts = tuple(map(int, data.split()))
    types = [(0, 0), (0, 1), (1, 0), (1, 1)]

    @lru_cache(maxsize=None)
    def search(a: int, b: int, c: int, d: int, last: int) -> int:
        best = 0
        arr = [a, b, c, d]
        for i, (start, end) in enumerate(types):
            if arr[i] and (last == 2 or last == start):
                arr[i] -= 1
                best = max(best, 1 + search(*arr, end))
                arr[i] += 1
        return best

    return str(search(*counts, 2))

def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("1 1 1 1\n"), edge("3 0 2 1\n"), stress("2 3 3 2\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
