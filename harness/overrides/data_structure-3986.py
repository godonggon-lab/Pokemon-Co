from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _good(word: str) -> bool:
    stack = []
    for ch in word:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return not stack


def _solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    return str(sum(1 for word in lines[1:1 + n] if _good(word)))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\nAB\n"),
        edge("1\nAA\n"),
        edge("2\nABBA\nABAB\n"),
        edge("3\nAABB\nBBAA\nABBA\n"),
        edge("4\nABAB\nAABB\nBBAABB\nAAAABB\n"),
        stress("5\n" + "A" * 20 + "\n" + "B" * 20 + "\n" + "AB" * 10 + "\n" + "AABB" * 5 + "\n" + "BAAB" * 5 + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
