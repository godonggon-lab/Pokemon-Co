from __future__ import annotations

from collections import Counter
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    lines = stdin.splitlines()
    out: list[str] = []
    for i in range(0, len(lines), 2):
        if i + 1 >= len(lines):
            break
        a = Counter(lines[i])
        b = Counter(lines[i + 1])
        chars = [ch * min(a[ch], b[ch]) for ch in sorted(set(a) & set(b))]
        out.append("".join(chars))
    return "\n".join(out)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "pretty\nwomen\nwalking\ndown\nthe\nstreet\n",
        "abc\nbcd\n",
        "aaaa\nbbbbb\n",
        "aabbcc\nabccdd\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    stdin = "abcdefghijklmnopqrstuvwxyz" * 5 + "\n" + "zyxwvutsrqponmlkjihgfedcba" * 3 + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
