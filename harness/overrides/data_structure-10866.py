from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1\nempty\n"),
        edge("3\npush_front 1\nfront\nback\n"),
        edge("5\npush_back 1\npush_front 2\nfront\nback\nsize\n"),
        edge("6\npop_front\npush_back 1\npush_back 2\npop_back\npop_front\npop_front\n"),
        edge("6\npush_front 3\npush_back 4\npop_front\npop_back\nempty\nfront\n"),
        stress("10\npush_back 1\npush_front 2\npush_back 3\nfront\nback\npop_front\npop_back\nsize\npop_front\nempty\n"),
    ]
