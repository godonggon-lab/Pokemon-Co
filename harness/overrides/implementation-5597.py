from __future__ import annotations

import random
from typing import List

from harness.cases import GeneratedCase, edge, stress


def _solve(stdin: str) -> str:
    submitted = set(map(int, stdin.split()))
    missing = [n for n in range(1, 31) if n not in submitted]
    return f"{missing[0]}\n{missing[1]}\n"


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    cases: List[GeneratedCase] = []
    missing_pairs = [
        (2, 8),
        (1, 30),
        (15, 16),
        (7, 29),
        (3, 4),
        (11, 23),
    ]
    for idx, missing in enumerate(missing_pairs):
        submitted = [n for n in range(1, 31) if n not in missing]
        rng = random.Random(f"5597:{idx}")
        rng.shuffle(submitted)
        stdin = "\n".join(map(str, submitted)) + "\n"
        cases.append(edge(stdin, _solve(stdin)))

    stdin = "\n".join(map(str, range(3, 31))) + "\n"
    cases.append(stress(stdin, _solve(stdin)))
    return cases
