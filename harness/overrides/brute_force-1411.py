from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _pattern(word: str) -> tuple[int, ...]:
    mapping = {}
    next_id = 0
    out = []
    for char in word:
        if char not in mapping:
            mapping[char] = next_id
            next_id += 1
        out.append(mapping[char])
    return tuple(out)


def _solve(data: str) -> str:
    lines = data.splitlines()
    words = lines[1:1 + int(lines[0])]
    patterns = [_pattern(word) for word in words]
    answer = 0
    for i in range(len(patterns)):
        for j in range(i + 1, len(patterns)):
            answer += patterns[i] == patterns[j]
    return str(answer)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("2\nab\ncd\n"),
        edge("3\naa\nab\ncc\n"),
        edge("4\nfoo\napp\nbar\nbaz\n"),
        edge("5\nabc\nbcd\naba\nxyx\nzzz\n"),
        edge("3\nabc\nabc\nabd\n"),
        stress("10\n" + "\n".join(["abc", "bcd", "cde", "aba", "xyx", "zzz", "abb", "cdd", "qwe", "rty"]) + "\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
