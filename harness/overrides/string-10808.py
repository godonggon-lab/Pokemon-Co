from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - 97] += 1
    return " ".join(map(str, counts))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "a\n",
        "baekjoon\n",
        "abcdefghijklmnopqrstuvwxyz\n",
        "zzzzzz\n",
        "abcabcabc\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "".join(chr(97 + (i % 26)) for i in range(1000))
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
