from __future__ import annotations
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    nums = list(map(int, data.split()))
    n = nums[0]
    cur = [0] * 6
    best_len = best_score = 0
    idx = 1
    for _ in range(n):
        a, b = nums[idx], nums[idx + 1]
        idx += 2
        nxt = [0] * 6
        nxt[a] = cur[a] + 1
        nxt[b] = max(nxt[b], cur[b] + 1)
        cur = nxt
        for score in range(1, 6):
            if cur[score] > best_len or (cur[score] == best_len and score < best_score):
                best_len, best_score = cur[score], score
    return f"{best_len} {best_score}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n1 2\n"),
        edge("3\n1 1\n1 2\n1 3\n"),
        edge("4\n5 4\n4 5\n5 5\n1 5\n"),
        edge("5\n2 3\n2 4\n2 5\n1 2\n2 2\n"),
        edge("4\n3 4\n4 3\n3 4\n4 3\n"),
        stress("20\n" + "\n".join(f"{i%5+1} {(i+2)%5+1}" for i in range(20)) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
