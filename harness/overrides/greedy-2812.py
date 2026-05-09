from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("2 1\n12\n"),
        edge("4 2\n1924\n"),
        edge("6 3\n123123\n"),
        edge("10 4\n4177252841\n"),
        edge("5 2\n99999\n"),
        stress("12 6\n987654321234\n"),
    ]
