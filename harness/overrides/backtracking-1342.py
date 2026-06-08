from __future__ import annotations
from collections import Counter
from typing import List
from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    counts = Counter(stdin.strip())
    n = sum(counts.values())
    answer = 0

    def dfs(prev: str, depth: int) -> None:
        nonlocal answer
        if depth == n:
            answer += 1
            return
        for ch in list(counts):
            if counts[ch] == 0 or ch == prev:
                continue
            counts[ch] -= 1
            dfs(ch, depth + 1)
            counts[ch] += 1

    dfs("", 0)
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [edge("a\n"), edge("aa\n"), edge("ab\n"), edge("abc\n"), edge("aabb\n"), stress("aabbccd\n")]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
