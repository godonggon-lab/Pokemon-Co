from __future__ import annotations

from typing import List
from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("3 3\n...\n.1.\n...\n"),
        edge("4 5\n.....\n.999.\n.9.9.\n.....\n"),
        stress("5 6\n......\n.3333.\n.3993.\n.3333.\n......\n"),
    ]
