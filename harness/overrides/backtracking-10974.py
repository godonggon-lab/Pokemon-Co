from __future__ import annotations

import itertools
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    n = int(stdin)
    return "\n".join(" ".join(map(str, p)) for p in itertools.permutations(range(1, n + 1)))


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases = [
        edge("1\n"),
        edge("2\n"),
        edge("3\n"),
        edge("4\n"),
        edge("5\n"),
        stress("6\n"),
    ]
    return [{**case, "expected": _solve(case["input"])} for case in cases]
