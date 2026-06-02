from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(data: str) -> str:
    document, word = data.splitlines()
    index = answer = 0
    while index <= len(document) - len(word):
        if document[index:index + len(word)] == word:
            answer += 1
            index += len(word)
        else:
            index += 1
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("abababa\naba\n"),
        edge("aaaaa\naa\n"),
        edge("abc\nz\n"),
        edge("hellohello\nhello\n"),
        stress(("abc" * 100) + "\nabc\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
