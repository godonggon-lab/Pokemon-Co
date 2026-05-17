from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    substrings: set[str] = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return str(len(substrings))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "ababc\n",
        "a\n",
        "aaaaa\n",
        "abcde\n",
        "banana\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "abcde" * 40
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
