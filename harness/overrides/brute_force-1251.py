from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    word = data.strip()
    best = None
    for i in range(1, len(word) - 1):
        for j in range(i + 1, len(word)):
            candidate = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
            if best is None or candidate < best:
                best = candidate
    return best or ""


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("mobitel\n"),
        edge("abc\n"),
        edge("zyx\n"),
        edge("abcdef\n"),
        edge("banana\n"),
        stress("abcdefghijklmnop\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
