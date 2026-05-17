from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    s = stdin.strip()
    return "\n".join(sorted(s[i:] for i in range(len(s))))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "baekjoon\n",
        "a\n",
        "banana\n",
        "aaaaa\n",
        "zyxwv\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = "abracadabra" * 20
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
