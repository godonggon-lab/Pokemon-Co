from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    return "1" if s == s[::-1] else "0"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "level\n",
        "baekjoon\n",
        "a\n",
        "abccba\n",
        "abcba\n",
        "abcdcba\n",
        "abcddcbae\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    palindrome = "a" * 500 + "b" + "a" * 500
    cases.append(stress(palindrome + "\n", _solve(palindrome + "\n")))
    return cases
