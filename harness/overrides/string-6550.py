from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def is_subsequence(s: str, t: str) -> bool:
    idx = 0
    for ch in t:
        if idx < len(s) and s[idx] == ch:
            idx += 1
    return idx == len(s)


def expected(stdin: str) -> str:
    out = []
    for line in stdin.strip().splitlines():
        s, t = line.split()
        out.append("Yes" if is_subsequence(s, t) else "No")
    return "\n".join(out) + "\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["abc ahbgdc\n", "axc ahbgdc\n", "a a\nabc abc\n", "ace abcde\naec abcde\n", "long short\nshort longershort\n", "abc abcabc\nxyz xaybzc\n"]
    return [edge(stdin, expected(stdin)) for stdin in inputs[:-1]] + [stress(inputs[-1], expected(inputs[-1]))]
