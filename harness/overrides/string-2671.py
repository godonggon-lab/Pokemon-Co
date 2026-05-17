from __future__ import annotations

import re
from typing import List

from harness.cases import GeneratedCase, edge, stress


PATTERN = re.compile(r"(100+1+|01)+\Z")


def _solve(stdin: str) -> str:
    s = stdin.strip()
    return "SUBMARINE" if PATTERN.fullmatch(s) else "NOISE"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    inputs = [
        "10010111\n",
        "011000100110001\n",
        "0110001011001\n",
        "01\n",
        "1001\n",
        "100\n",
        "010101\n",
    ]
    cases = [edge(stdin, _solve(stdin)) for stdin in inputs]
    s = ("10000111101" * 20) + "01"
    cases.append(stress(s + "\n", _solve(s + "\n")))
    return cases
