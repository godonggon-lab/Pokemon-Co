from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    return "a" * int(stdin.strip())


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "2\n", "5\n", "10\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("1000\n", _solve("1000\n")))
    return cases
