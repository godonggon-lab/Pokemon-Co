from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nempty\n"),
        edge("3\npush 1\ntop\npop\n"),
        edge("5\npop\npush 2\npush 3\nsize\ntop\n"),
        edge("6\npush 1\npush 2\npop\npop\npop\nempty\n"),
        edge("4\npush 9\nsize\ntop\nempty\n"),
        stress("10\npush 1\npush 2\npush 3\npop\ntop\nsize\npop\npop\npop\nempty\n"),
    ]
