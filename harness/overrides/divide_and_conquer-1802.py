from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _valid(text: str) -> bool:
    if len(text) == 1:
        return True
    mid = len(text) // 2
    for i in range(mid):
        if text[i] == text[-1 - i]:
            return False
    return _valid(text[:mid]) and _valid(text[mid + 1:])


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    return "\n".join("YES" if _valid(text) else "NO" for text in lines[1:1 + n])


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n0\n"),
        edge("2\n0\n1\n"),
        edge("3\n000\n010\n101\n"),
        edge("4\n001\n011\n100\n110\n"),
        edge("5\n0000000\n0001000\n0101010\n1010101\n1110111\n"),
        stress("6\n0\n1\n001\n110\n0001000\n1110111\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
