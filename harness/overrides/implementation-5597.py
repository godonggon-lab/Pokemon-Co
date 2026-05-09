from __future__ import annotations

import random
from typing import List

from harness.cases import edge, GeneratedCase


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
        cases.append(edge("\n".join(map(str, submitted)) + "\n"))

    return cases
