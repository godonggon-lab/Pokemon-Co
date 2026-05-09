from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nempty\n", "1\n"),
        edge("3\npush 1\nfront\nback\n", "1\n1\n"),
        edge("5\npush 1\npush 2\npop\npop\npop\n", "1\n2\n-1\n"),
        edge("6\nsize\nempty\npush 3\nsize\nfront\nback\n", "0\n1\n1\n3\n3\n"),
        edge("4\npush 9\npop\nempty\nback\n", "9\n1\n-1\n"),
        stress("10\npush 1\npush 2\npush 3\npop\nfront\nback\nsize\npop\npop\nempty\n", "1\n2\n3\n2\n2\n3\n1\n"),
    ]
