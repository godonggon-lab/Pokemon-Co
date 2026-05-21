from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    bits = bin(int(stdin.strip()) + 1)[3:]
    return "".join("4" if bit == "0" else "7" for bit in bits)


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = ["1\n", "2\n", "3\n", "4\n", "7\n", "10\n"]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    cases.append(stress("1000000000\n", _solve("1000000000\n")))
    return cases
