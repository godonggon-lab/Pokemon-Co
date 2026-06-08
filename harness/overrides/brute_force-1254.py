from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    text = data.strip()
    for index in range(len(text)):
        tail = text[index:]
        if tail == tail[::-1]:
            return str(len(text) + index)
    return str(len(text) * 2 - 1)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("abab\n"),
        edge("abacaba\n"),
        edge("a\n"),
        edge("abcd\n"),
        edge("aaaa\n"),
        stress("abcdeffedcbaxyz\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
