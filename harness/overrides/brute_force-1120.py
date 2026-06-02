from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    left, right = data.split()
    answer = len(left)
    for start in range(len(right) - len(left) + 1):
        answer = min(answer, sum(a != b for a, b in zip(left, right[start:start + len(left)])))
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("adaabc aababbc\n"),
        edge("abc abc\n"),
        edge("abc zzzabczzz\n"),
        edge("aaaa bbbbb\n"),
        stress("abcde " + "x" * 20 + "abzde" + "y" * 20 + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
