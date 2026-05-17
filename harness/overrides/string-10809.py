from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    return " ".join(str(s.find(chr(97 + i))) for i in range(26))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "baekjoon\n",
        "abcdefghijklmnopqrstuvwxyz\n",
        "aaaaa\n",
        "zyxwvutsrqponmlkjihgfedcba\n",
        "abcabc\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "".join(chr(97 + (i % 26)) for i in range(1000))
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
